"""
Translation module using MiniMax API
"""

import re
import time
import requests
from typing import Optional, List, Tuple
from .config import (
    MINIMAX_API_KEY,
    MINIMAX_API_URL,
    MINIMAX_MODEL,
    MINIMAX_MAX_TOKENS,
)


class Translator:
    """Translator using MiniMax API"""

    # Max chars per chunk (留空间给prompt)
    MAX_CHUNK_SIZE = 8000

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

    def extract_code_blocks(self, text: str) -> List[str]:
        """Extract code blocks to protect from translation."""
        pattern = r'(```[\s\S]*?```|`[^`]+`)'
        return re.findall(pattern, text)

    def translate(self, text: str, force: bool = False) -> str:
        """
        Translate text to Chinese. Handles long content by chunking.
        """
        if not text or len(text.strip()) < 10:
            return text

        if self.is_chinese(text) and not force:
            return text

        # Extract and protect code blocks
        code_blocks = self.extract_code_blocks(text)
        placeholder_map = {}
        for i, block in enumerate(code_blocks):
            placeholder = f"__TRANSLATION_PLACEHOLDER_{i}__"
            placeholder_map[placeholder] = block
            text = text.replace(block, placeholder)

        # Chunk if needed
        if len(text) > self.MAX_CHUNK_SIZE:
            translated = self._translate_chunked(text)
        else:
            try:
                translated = self._call_api(text)
            except Exception as e:
                print(f"Translation error: {e}")
                return text

        # Restore code blocks
        for placeholder, block in placeholder_map.items():
            translated = translated.replace(placeholder, block)

        return translated

    def _translate_chunked(self, text: str) -> str:
        """Translate long text by chunking."""
        chunks = self._split_into_chunks(text)
        results = []

        print(f"Translating {len(chunks)} chunks...")
        for i, chunk in enumerate(chunks):
            print(f"  Chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...")
            for attempt in range(3):
                try:
                    translated = self._call_api(chunk)
                    results.append(translated)
                    break
                except Exception as e:
                    print(f"  Chunk {i+1} attempt {attempt+1} failed: {e}")
                    if attempt == 2:
                        results.append(chunk)  # Use original on failure
                    time.sleep(2)

        return '\n\n'.join(results)

    def _split_into_chunks(self, text: str) -> List[str]:
        """Split text into chunks at paragraph/sentence boundaries."""
        if len(text) <= self.MAX_CHUNK_SIZE:
            return [text]

        chunks = []
        # Split by double newlines (paragraphs)
        paragraphs = text.split('\n\n')
        current_chunk = ''

        for para in paragraphs:
            if len(current_chunk) + len(para) + 2 <= self.MAX_CHUNK_SIZE:
                current_chunk += para + '\n\n'
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                # If single paragraph is too long, split by sentences
                if len(para) > self.MAX_CHUNK_SIZE:
                    sentences = re.split(r'(?<=[.!?。！？])\s+', para)
                    current_chunk = ''
                    for sent in sentences:
                        if len(current_chunk) + len(sent) + 1 <= self.MAX_CHUNK_SIZE:
                            current_chunk += sent + ' '
                        else:
                            if current_chunk:
                                chunks.append(current_chunk.strip())
                            current_chunk = sent + ' '
                else:
                    current_chunk = para + '\n\n'

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

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
            "max_tokens": self.max_tokens
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            json=payload,
            timeout=120  # Longer timeout for API call
        )

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code} - {response.text[:200]}")

        result = response.json()
        choice = result['choices'][0]
        message = choice.get('message', {})
        content = message.get('content', '')
        if not content:
            content = message.get('reasoning_content', '')
        return content

    def translate_batch(self, texts: list, delay: float = 1.0) -> list:
        """Translate multiple texts with delay between requests."""
        results = []
        for i, text in enumerate(texts):
            print(f"Translating {i+1}/{len(texts)}...")
            results.append(self.translate(text))
            if i < len(texts) - 1:
                time.sleep(delay)
        return results


# Singleton instance
_translator = None


def get_translator() -> Translator:
    """Get or create singleton translator instance"""
    global _translator
    if _translator is None:
        _translator = Translator()
    return _translator