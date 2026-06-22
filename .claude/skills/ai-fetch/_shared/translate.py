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

    # Only translate short text (titles, abstracts)
    MAX_TRANSLATE_LEN = 2000

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
        """Translate text to Chinese (only for short text)."""
        if not text or len(text.strip()) < 10:
            return text

        if self.is_chinese(text) and not force:
            return text

        # Only translate short text
        if len(text) > self.MAX_TRANSLATE_LEN:
            # For long content, return as-is (skip translation)
            return text

        try:
            return self._call_api(text)
        except Exception as e:
            print(f"Translation error: {e}")
            return text

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
            "max_tokens": min(2000, len(text) * 2)
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