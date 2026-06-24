#!/usr/bin/env python3
"""Generate index.md for Google I/O 2026 - simplified version"""

import os
import re
from pathlib import Path
from collections import defaultdict

SESSIONS_DIR = Path(__file__).parent
OUTPUT_FILE = SESSIONS_DIR / "index.md"


def parse_frontmatter(content: str) -> dict:
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value.startswith('[') and value.endswith(']'):
                frontmatter[key] = [s.strip() for s in value[1:-1].split(',')]
            else:
                frontmatter[key] = value
    return frontmatter


def load_sessions() -> list[dict]:
    sessions = []
    for md_file in SESSIONS_DIR.glob("[0-9]*.md"):
        if md_file.name in ["generate_index.py", "index.md"]:
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)
            if not fm.get('title'):
                continue
            match = re.match(r'^(\d+)', md_file.stem)
            seq_num = int(match.group(1)) if match else 0
            session = {
                'filename': md_file.name,
                'seq': seq_num,
                'title': fm.get('title', ''),
                'title_zh': fm.get('title_zh', ''),
                'date': fm.get('date', ''),
                'time': fm.get('time', ''),
                'track': fm.get('track', ''),
                'type': fm.get('type', ''),
                'level': fm.get('level', ''),
                'speakers': fm.get('speakers', []),
                'video': fm.get('video', ''),
            }
            sessions.append(session)
        except Exception as e:
            print(f"Error reading {md_file.name}: {e}")
    sessions.sort(key=lambda s: s['seq'])
    return sessions


def is_keynote(session: dict) -> bool:
    return 'keynote' in session['type'].lower() or '主题演讲' in session['type']


def is_google_keynote(session: dict) -> bool:
    if not is_keynote(session):
        return False
    return 'google' in session['title'].lower() or 'google' in session['type'].lower()


def generate_index() -> str:
    sessions = load_sessions()

    # 只显示大会当天内容 (01-65)
    main_sessions = [s for s in sessions if s['seq'] <= 65]

    # 分类
    day1_keynotes = [s for s in main_sessions if is_keynote(s) and s['date'] == '2026-05-19']
    day1_google_keynote = [s for s in day1_keynotes if is_google_keynote(s)]
    day1_dev_keynote = [s for s in day1_keynotes if not is_google_keynote(s)]

    # Day1下午并行 (15:30-16:15)
    afternoon_parallel = [s for s in main_sessions if s['date'] == '2026-05-19'
                          and '15:30' in s['time'] and '16:15' in s['time']
                          and not is_keynote(s)]

    # Day1下午其他 (16:30-17:15)
    afternoon_other = [s for s in main_sessions if s['date'] == '2026-05-19'
                       and '16:30' in s['time'] and '17:15' in s['time']
                       and not is_keynote(s)]

    # Day2
    day2_sessions = [s for s in main_sessions if s['date'] in ['2026-05-20', '2026-05-21']]

    lines = []

    # ========== 大会基础信息 ==========
    lines.extend([
        "# Google I/O 2026 完整分时段议程总表",
        "",
        "## 大会基础信息",
        "",
        "- **举办地点**: 加州山景城 Shoreline Amphitheatre",
        "- **举办日期**: 2026-05-19（Day1）、2026-05-20（Day2）",
        "- **时区**: PT 太平洋时间；北京时间 = PT+15 小时",
        "- **核心主题**: Agentic Era（智能体时代）",
        f"- **议题总数**: {len(main_sessions)} 场",
        "",
    ])

    # ========== Day1 Keynotes ==========
    lines.extend([
        "---",
        "",
        "## 一、Day1 主会场 Keynote",
        "",
        "| 序号 | 场次 | PT时间 | 主讲人 |",
        "| --- | --- | --- | --- |",
    ])

    for session in day1_google_keynote + day1_dev_keynote:
        seq = f"{session['seq']:02d}"
        time = session['time'].replace(' PT', '').strip()
        speakers = session['speakers']
        if isinstance(speakers, list):
            speakers = ', '.join(speakers[:3]) + ('...' if len(speakers) > 3 else '')
        elif not speakers:
            speakers = '-'
        title = session['title_zh'] or session['title']
        lines.append(f"| {seq} | [{title}](sessions/{session['filename']}) | {time} | {speakers} |")

    # ========== Day1 下午并行 ==========
    lines.extend([
        "",
        "---",
        "",
        "## 二、Day1 下午并行分会场",
        "",
        "| 序号 | 议题 | 时间 | 分类 | 演讲者 |",
        "| --- | --- | --- | --- | --- |",
    ])

    for session in afternoon_parallel + afternoon_other:
        seq = f"{session['seq']:02d}"
        time = session['time'].replace(' PT', '').strip()
        title = session['title_zh'] or session['title']
        track = session['track'] or '-'
        speakers = session['speakers']
        if isinstance(speakers, list):
            speakers = ', '.join(speakers[:2]) + ('...' if len(speakers) > 2 else '')
        elif not speakers:
            speakers = '-'
        lines.append(f"| {seq} | [{title}](sessions/{session['filename']}) | {time} | {track} | {speakers} |")

    # ========== Day2 ==========
    lines.extend([
        "",
        "---",
        "",
        "## 三、Day2 深度技术分会场",
        "",
    ])

    # 按日期分组
    day2_by_date = defaultdict(list)
    for s in day2_sessions:
        day2_by_date[s['date']].append(s)

    for date in sorted(day2_by_date.keys()):
        date_sessions = day2_by_date[date]
        date_label = "2026-05-20" if date == "2026-05-20" else "2026-05-21"

        lines.extend([
            f"### {date_label}（{len(date_sessions)}场）",
            "",
            "| 序号 | 议题 | 时间 | 分类 | 演讲者 |",
            "| --- | --- | --- | --- | --- |",
        ])

        for session in date_sessions:
            seq = f"{session['seq']:02d}"
            time = session['time'].replace(' PT', '').strip()
            if not time or time == 'PT':
                time = '-'
            title = session['title_zh'] or session['title']
            track = session['track'] or '-'
            speakers = session['speakers']
            if isinstance(speakers, list):
                speakers = ', '.join(speakers[:2]) + ('...' if len(speakers) > 2 else '')
            elif not speakers:
                speakers = '-'
            lines.append(f"| {seq} | [{title}](sessions/{session['filename']}) | {time} | {track} | {speakers} |")
        lines.append("")

    # ========== 发布时间线 ==========
    lines.extend([
        "---",
        "",
        "## 四、关键发布落地时间线",
        "",
        "| 产品/技术 | 发布状态 | 上线时间 |",
        "| --- | --- | --- |",
        "| Gemini 3.5 Flash | 正式GA | I/O当日开放 |",
        "| Gemini 3.5 Pro | 内测预览 | 2026年6月 |",
        "| Gemini Spark | 灰度测试 | 2026夏季 |",
        "| Project Mariner | 预览版 | 2026夏季 |",
        "| Android 17 | 开发者预览 | 2026下半年 |",
        "| MCP开发者套件 | 正式开放 | I/O当日 |",
        "| Antigravity 2.0 | GA商用 | I/O当日 |",
        "",
    ])

    return '\n'.join(lines)


def main():
    print("生成 index.md...")
    content = generate_index()
    # 只写入上级目录
    parent_index = SESSIONS_DIR.parent / "index.md"
    parent_index.write_text(content, encoding='utf-8')
    print(f"完成: {parent_index}")


if __name__ == '__main__':
    main()