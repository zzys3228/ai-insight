#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Translate YouTube subtitles to Chinese for missing session files.
"""

import re
import json
import subprocess
import tempfile
import os
from pathlib import Path

# MiniMax API config
MINIMAX_API_URL = "https://api.minimaxi.com/anthropic/v1/messages"
MINIMAX_MODEL = "MiniMax-M2.7"
MINIMAX_API_KEY = "REDACTED_API_KEY"

def parse_srt(filepath):
    """Parse SRT file and return clean text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')
    text_parts = []

    for line in lines:
        line = line.strip()
        # Skip timestamps and numbers
        if '-->' in line or line.isdigit():
            continue
        # Clean HTML tags
        line = re.sub(r'<[^>]+>', '', line)
        # Skip empty lines
        if line:
            text_parts.append(line)

    return ' '.join(text_parts)

def translate_text(text, chunk_size=8000):
    """Translate text to Chinese using MiniMax API."""
    if len(text) <= chunk_size:
        return _call_api(text)

    # Split into chunks
    parts = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        try:
            translated = _call_api(chunk)
            parts.append(translated)
        except Exception as e:
            print(f"Translation error: {e}")
            parts.append(chunk)

    return '\n\n'.join(parts)

def _call_api(text):
    """Call MiniMax API to translate."""
    request_data = json.dumps({
        'model': MINIMAX_MODEL,
        'max_tokens': 8192,
        'messages': [{
            'role': 'user',
            'content': f'将以下英文字幕翻译成中文口语，保持自然的对话风格，只返回翻译结果不要解释：\n\n{text}'
        }]
    }, ensure_ascii=False)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        f.write(request_data)
        temp_req_path = f.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        temp_out_path = f.name

    try:
        cmd = [
            'curl', '-s', '--max-time', '120', '-X', 'POST',
            MINIMAX_API_URL,
            '-H', f'Authorization: Bearer {MINIMAX_API_KEY}',
            '-H', 'Content-Type: application/json',
            '-d', '@' + temp_req_path,
            '-o', temp_out_path
        ]

        subprocess.run(cmd, timeout=150)

        with open(temp_out_path, 'rb') as f:
            raw_bytes = f.read()

        data = json.loads(raw_bytes)

        # Extract text from response
        text_result = None
        for block in data.get('content', []):
            if isinstance(block, dict) and block.get('type') == 'text':
                text_result = block.get('text', '')
                break

        if text_result:
            return text_result.strip()
        return text

    finally:
        for p in [temp_req_path, temp_out_path]:
            if os.path.exists(p):
                os.remove(p)

def update_session_file(filepath, translated_transcript):
    """Update session file with translated transcript."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace placeholder with actual translation
    pattern = r'## 📝 完整文字稿\n\n好的，我来把它翻译成自然的中文口语：\n---'
    replacement = f'## 📝 完整文字稿\n\n{translated_transcript}\n\n---'

    content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    sessions_dir = Path(__file__).parent

    # Files to process
    files_to_translate = [
        ('03-pa-keynote-1.md', 'temp_03.en.srt'),
        ('06-technical-session-46.md', 'temp_caption.en.srt'),
        ('20-pa-keynote-16.md', 'temp_20.en.srt'),
    ]

    for md_file, srt_file in files_to_translate:
        md_path = sessions_dir / md_file
        srt_path = sessions_dir / srt_file

        if not srt_path.exists():
            print(f"Missing SRT file: {srt_file}")
            continue

        print(f"Processing {md_file}...")

        # Parse SRT
        text = parse_srt(srt_path)
        print(f"  Extracted {len(text)} chars from SRT")

        # Translate
        translated = translate_text(text)
        print(f"  Translated to {len(translated)} chars")

        # Update file
        update_session_file(md_path, translated)
        print(f"  Updated {md_file}")

        # Cleanup temp SRT
        srt_path.unlink()

    print("\nDone!")

if __name__ == '__main__':
    main()