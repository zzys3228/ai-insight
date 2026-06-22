"""
Translation module using MiniMax API
"""

import re
import time
import requests
from typing import Optional, List
from .config import (
    MINIMAX_API_KEY,
    MINIMAX_API_URL,
    MINIMAX_MODEL,
    MINIMAX_MAX_TOKENS,
)


class Translator:
    """Translator using MiniMax API"""

    # Translate up to 10000 chars, chunk longer content
    MAX_TRANSLATE_LEN = 10000
    CHUNK_SIZE = 8000

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or MINIMAX_API_KEY
        self.api_url = MINIMAX_API_URL
        self.model = MINIMAX_MODEL
        self.max_tokens = MINIMAX_MAX_TOKENS

    def is_chinese(self, text: str) -> bool:
        """Check if text is primarily Chinese."""
        if not text or len(text.strip()) < 10:
            return False
        chinese_chars = len(re.findall(r'[一-鿿]', text))
        total_chars = len(text.strip())
        return chinese_chars / max(total_chars, 1) > 0.3

    def translate(self, text: str, force: bool = False) -> str:
        """Translate text to Chinese (with chunking for long content)."""
        if not text or len(text.strip()) < 10:
            return text

        if self.is_chinese(text) and not force:
            return text

        # Chunk long content
        if len(text) > self.CHUNK_SIZE:
            return self._translate_chunked(text)

        try:
            return self._call_api(text)
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    def _translate_chunked(self, text: str) -> str:
        """Translate long content by chunking."""
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = []
        current_len = 0

        for para in paragraphs:
            para_len = len(para)
            if current_len + para_len > self.CHUNK_SIZE and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [para]
                current_len = para_len
            else:
                current_chunk.append(para)
                current_len += para_len

        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))

        # Translate each chunk
        results = []
        for i, chunk in enumerate(chunks):
            print(f"  Translating chunk {i+1}/{len(chunks)}...")
            try:
                translated = self._call_api(chunk)
                results.append(translated)
            except Exception as e:
                print(f"  Chunk {i+1} failed: {e}")
                results.append(chunk)
            time.sleep(0.5)  # Rate limit

        return '\n\n'.join(results)

    def _call_api(self, text: str) -> str:
        """Call MiniMax API for translation."""
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": f"Translate to Chinese, keep technical terms accurate:\n\n{text}"
                }
            ],
            "max_tokens": min(8192, len(text) * 2)
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")

        result = response.json()
        choices = result.get('choices', [])
        if choices:
            message = choices[0].get('message', {})
            content = message.get('content', '')
            if content:
                return content.strip()
        return text


# Singleton instance
_translator = None


def get_translator() -> Translator:
    """Get or create singleton translator instance"""
    global _translator
    if _translator is None:
        _translator = Translator()
    return _translator