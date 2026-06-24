"""
Translation module using MiniMax API via curl subprocess.
This avoids Python's requests library encoding issues on Windows.
"""

import subprocess
import json
import re
import time
import tempfile
from pathlib import Path
from typing import Optional
from .config import MINIMAX_API_KEY, MINIMAX_API_URL, MINIMAX_MODEL


class Translator:
    CHUNK_SIZE = 1500

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or MINIMAX_API_KEY
        self.api_url = MINIMAX_API_URL
        self.model = MINIMAX_MODEL

    def is_chinese(self, text: str) -> bool:
        if not text or len(text.strip()) < 10:
            return False
        chinese = len(re.findall(r'[一-鿿]', text))
        return chinese / len(text.strip()) > 0.3

    def translate(self, text: str) -> str:
        if not text or len(text.strip()) < 10:
            return text
        if self.is_chinese(text):
            return text
        if len(text) > self.CHUNK_SIZE:
            return self._chunked(text)
        return self._call(text)

    def _chunked(self, text: str) -> str:
        parts = []
        for i in range(0, len(text), self.CHUNK_SIZE):
            chunk = text[i:i+self.CHUNK_SIZE]
            try:
                parts.append(self._call(chunk))
            except Exception as e:
                parts.append(chunk)
            time.sleep(0.2)
        return '\n'.join(parts)

    def _call(self, text: str) -> str:
        """Call MiniMax API via curl subprocess for correct UTF-8 handling."""
        import tempfile
        import os

        try:
            # Write JSON to temp file to avoid command line encoding issues
            max_tokens_value = max(500, min(4096, len(text) * 4))
            request_data = json.dumps({
                'model': self.model,
                'max_tokens': max_tokens_value,
                'messages': [{'role': 'user', 'content': f'翻译成中文，只返回翻译结果，不要解释：\n\n{text}'}]
            }, ensure_ascii=False)

            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
                f.write(request_data)
                temp_req_path = f.name

            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
                temp_out_path = f.name

            # Use @file syntax to avoid command line encoding issues
            cmd = [
                'curl', '-s', '--max-time', '60', '-X', 'POST',
                self.api_url,
                '-H', f'Authorization: Bearer {self.api_key}',
                '-H', 'Content-Type: application/json',
                '-d', '@' + temp_req_path,
                '-o', temp_out_path
            ]

            subprocess.run(cmd, timeout=90)

            # Read response
            with open(temp_out_path, 'rb') as f:
                raw_bytes = f.read()

            # Parse JSON
            data = json.loads(raw_bytes)

            # Extract text from response (supports both OpenAI and Anthropic formats)
            text_result = None

            # Anthropic format
            for block in data.get('content', []):
                if isinstance(block, dict) and block.get('type') == 'text':
                    text_result = block.get('text', '')
                    break

            # OpenAI format fallback
            if text_result is None:
                text_result = data.get('choices', [{}])[0].get('message', {}).get('content', '')

            if text_result:
                return self._clean_translation(text_result)

            return text

        except subprocess.TimeoutExpired:
            return text
        except json.JSONDecodeError:
            return text
        except Exception as e:
            print(f"Translation error: {e}")
            return text
        finally:
            # Clean up temp files
            for p in [temp_req_path, temp_out_path]:
                if os.path.exists(p):
                    try:
                        os.remove(p)
                    except Exception:
                        pass

    def _clean_translation(self, text: str) -> str:
        """Clean up translation output."""
        # Remove markdown formatting
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = text.strip()
        return text


_tr = None

def get_translator() -> Translator:
    global _tr
    if _tr is None:
        _tr = Translator()
    return _tr
