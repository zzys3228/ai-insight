#!/usr/bin/env python3
"""
Script to clean VTT subtitles and translate using MiniMax API
"""
import re
import requests
import json
import os
from pathlib import Path

# Load .env.local if exists
_env_local = Path(__file__).parent.parent.parent.parent.parent.parent / '.env.local'
if _env_local.exists():
    with open(_env_local, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())

# API configuration (from environment)
API_URL = os.environ.get('MINIMAX_API_URL', 'https://api.minimaxi.com/anthropic/v1/messages')
API_KEY = os.environ.get('MINIMAX_API_KEY', '')
MODEL = os.environ.get('MINIMAX_MODEL', 'MiniMax-M2.7')

def clean_vtt(vtt_content):
    """Clean VTT file - remove timestamps and duplicate lines"""
    lines = vtt_content.split('\n')
    cleaned_lines = []
    prev_line = ""

    # Skip WEBVTT header and metadata
    skip_header = True

    for line in lines:
        # Skip header lines
        if skip_header:
            if line.strip() == "" or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
                continue
            if re.match(r'^\d{2}:\d{2}:\d{2}', line):
                skip_header = False

        # Skip timestamp lines and empty lines
        if re.match(r'^\d{2}:\d{2}:\d{2}', line):
            continue
        if line.strip() == "":
            continue

        # Remove HTML-like tags
        line = re.sub(r'<[^>]+>', '', line)

        # Convert HTML entities
        line = line.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')

        # Skip music/sound markers
        if '[music]' in line.lower() or '[applause]' in line.lower():
            continue

        # Skip duplicate lines
        if line.strip() == prev_line.strip():
            continue

        if line.strip():
            cleaned_lines.append(line.strip())
            prev_line = line

    return ' '.join(cleaned_lines)

def translate_text(text, chunk_size=1500):
    """Translate text using MiniMax API in chunks"""
    # Split text into chunks
    chunks = []
    current_chunk = ""
    sentences = text.split('. ')

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + '. '
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + '. '

    if current_chunk:
        chunks.append(current_chunk.strip())

    translated_chunks = []

    for i, chunk in enumerate(chunks):
        print(f"Translating chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...")

        headers = {
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01"
        }

        payload = {
            "model": MODEL,
            "max_tokens": 4000,
            "messages": [
                {
                    "role": "user",
                    "content": f"""请将以下英文演讲字幕翻译成自然的中文口语。保留技术术语原文（如Flutter、Dart、Gemini、Material Design、Agent、Anti-Gravity等）。不要添加任何解释或说明，直接输出翻译结果：

{chunk}"""
                }
            ]
        }

        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
            result = response.json()

            if 'content' in result:
                translated = result['content'][0]['text']
                translated_chunks.append(translated)
            elif 'error' in result:
                print(f"API Error: {result['error']}")
                translated_chunks.append(chunk)  # Keep original if translation fails
            else:
                print(f"Unexpected response: {result}")
                translated_chunks.append(chunk)
        except Exception as e:
            print(f"Translation error: {e}")
            translated_chunks.append(chunk)

    return '\n\n'.join(translated_chunks)

def process_file(vtt_path, output_md_path, title):
    """Process a VTT file and add translation to markdown"""
    print(f"\nProcessing: {vtt_path}")

    # Read VTT file
    with open(vtt_path, 'r', encoding='utf-8') as f:
        vtt_content = f.read()

    print(f"VTT file size: {len(vtt_content)} chars")

    # Clean VTT
    cleaned_text = clean_vtt(vtt_content)
    print(f"Cleaned text size: {len(cleaned_text)} chars")

    # Translate
    translated_text = translate_text(cleaned_text)
    print(f"Translated text size: {len(translated_text)} chars")

    # Read existing markdown
    with open(output_md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Find the complete transcript section
    transcript_marker = "## 📝 完整文字稿"  # ## 📝 完整文字稿

    if transcript_marker in md_content:
        # Find the position and replace/append content
        parts = md_content.split(transcript_marker)
        if len(parts) >= 2:
            # Keep front matter and content before transcript
            front_content = parts[0]

            # Find where to insert - after the marker and any existing partial content
            remaining = parts[1] if len(parts) > 1 else ""

            # Build new content
            new_transcript_section = f"\n\n{translated_text}\n\n---\n\n*原文链接: [{title}](https://www.youtube.com/watch?v={os.path.basename(vtt_path).split('.')[0]})"

            # Check if there's already content we need to preserve or replace
            # Look for the next major section marker
            new_md_content = front_content + transcript_marker + new_transcript_section
        else:
            new_md_content = md_content + "\n\n" + transcript_marker + "\n\n" + translated_text
    else:
        # Add new section
        new_md_content = md_content + "\n\n" + transcript_marker + "\n\n" + translated_text + "\n\n---\n\n*原文链接: [{title}](https://www.youtube.com/watch?v=" + os.path.basename(vtt_path).split('.')[1].split('.')[0] + ")"

    # Write updated markdown
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(new_md_content)

    print(f"Updated markdown file: {output_md_path}")
    print(f"Final file size: {len(new_md_content)} chars")

    return len(new_md_content)

if __name__ == "__main__":
    base_path = r"D:\aicoding\startup\ppt-test\ai-content-fetched\conference\google-io\2026\sessions"

    files_to_process = [
        {
            "vtt": "temp_1.en.vtt",
            "md": "06-technical-session-46.md",
            "title": "Agent-first workflows from prompt to production",
            "video_id": "CBL6KgCsQNY"
        },
        {
            "vtt": "temp_2.en.vtt",
            "md": "20-pa-keynote-16.md",
            "title": "A new era of discovery: AI and the frontiers of science",
            "video_id": "dgBLVm2L1P4"
        },
        {
            "vtt": "temp_3.en.vtt",
            "md": "25-workshop-3.md",
            "title": "Vibe once, run anywhere with Google Antigravity and Flutter",
            "video_id": "UNdQhnpm8GY"
        },
        {
            "vtt": "temp_4.en.vtt",
            "md": "28-technical-session-13.md",
            "title": "Make Material your own",
            "video_id": "HbAFGivZ158"
        }
    ]

    results = []
    for file_info in files_to_process:
        vtt_path = os.path.join(base_path, file_info["vtt"])
        md_path = os.path.join(base_path, file_info["md"])

        try:
            size = process_file(vtt_path, md_path, file_info["title"])
            results.append({
                "file": file_info["md"],
                "status": "success",
                "final_size": size
            })
        except Exception as e:
            results.append({
                "file": file_info["md"],
                "status": "failed",
                "error": str(e)
            })

    print("\n\n=== Results Summary ===")
    for r in results:
        if r["status"] == "success":
            print(f"{r['file']}: SUCCESS - {r['final_size']} chars")
        else:
            print(f"{r['file']}: FAILED - {r['error']}")