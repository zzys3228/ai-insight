"""
Academic Paper Fetcher

Fetches academic papers from arXiv and other sources.
Downloads PDF, parses content, and translates to Chinese.
"""

import sys
import os
import re
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from _shared.config import should_use_proxy, REQUEST_TIMEOUT, STORAGE_BASE
from _shared.translate import Translator
from _shared.utils import (
    parse_arxiv_id,
    get_arxiv_pdf_url,
    format_markdown_frontmatter,
    get_file_timestamp,
    extract_domain,
)


class AcademicFetcher:
    """Fetcher for academic papers"""

    def __init__(self, use_proxy: bool = False):
        self.translator = Translator()
        self.use_proxy = use_proxy
        self.delay = 1.0

    def _get(self, url: str, **kwargs) -> requests.Response:
        """Make GET request with proxy support"""
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {
                'http': 'http://127.0.0.1:26001',
                'https': 'http://127.0.0.1:26001'
            }

        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT, **kwargs)

    def fetch_arxiv_list(self, url: str) -> List[Dict]:
        """
        Fetch paper list from arXiv category page.

        Args:
            url: arXiv category URL (e.g., https://arxiv.org/list/cs.CL/recent)

        Returns:
            List of paper metadata
        """
        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch arXiv list: {response.status_code}")

        papers = self._parse_arxiv_list(response.text)
        return papers

    def _parse_arxiv_list(self, html: str) -> List[Dict]:
        """Parse arXiv category page to extract paper list"""
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, 'html.parser')
        papers = []

        # Find all dt elements (contain the link)
        dts = soup.find_all('dt')

        for dt in dts:
            # Find the abstract link
            link = dt.find('a', title='Abstract')
            if not link:
                continue

            href = link.get('href', '')
            paper_id_match = re.search(r'/abs/([0-9]+\.[0-9]+)', href)
            if not paper_id_match:
                continue

            paper_id = paper_id_match.group(1)

            # Find the corresponding dd element
            dd = dt.find_next_sibling('dd')
            if not dd:
                continue

            # Extract title from list-title
            title_elem = dd.find('div', class_='list-title')
            title = ''
            if title_elem:
                title = title_elem.get_text(strip=True)
                # Remove "Title:" prefix
                title = re.sub(r'^Title:\s*', '', title)

            # Extract authors
            authors_elem = dd.find('div', class_='list-authors')
            authors = ''
            if authors_elem:
                authors = authors_elem.get_text(strip=True)
                # Remove "Authors:" prefix
                authors = re.sub(r'^Authors:\s*', '', authors)

            # Extract subjects
            subjects_elem = dd.find('div', class_='list-subjects')
            subjects = ''
            if subjects_elem:
                subjects = subjects_elem.get_text(strip=True)
                subjects = re.sub(r'^Subjects:\s*', '', subjects)

            papers.append({
                'paper_id': paper_id,
                'url': f"https://arxiv.org/abs/{paper_id}",
                'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf",
                'title': title,
                'authors': authors,
                'subjects': subjects,
            })

        return papers

    def fetch_paper(self, paper_id: str, category: str = 'cs.CL') -> Dict:
        """
        Fetch complete paper content.

        Args:
            paper_id: arXiv paper ID (e.g., 2606.20527)
            category: Paper category (for storage path)

        Returns:
            Dictionary with paper content
        """
        # Fetch abstract from abs page
        abs_url = f"https://arxiv.org/abs/{paper_id}"
        response = self._get(abs_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch paper: {response.status_code}")

        paper_info = self._parse_arxiv_page(response.text, paper_id)

        # Download PDF
        pdf_path = self._download_pdf(paper_id)

        # Parse PDF
        pdf_text = self._parse_pdf(pdf_path)

        # Translate
        if pdf_text:
            translated_content = self._translate_content(pdf_text)
        else:
            translated_content = ''

        return {
            'paper_id': paper_id,
            'category': category,
            'abs_url': abs_url,
            'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf",
            'content': translated_content,
            'pdf_text': pdf_text,
            'metadata': paper_info,
        }

    def _parse_arxiv_page(self, html: str, paper_id: str) -> Dict:
        """Parse arXiv abstract page"""
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, 'html.parser')
        info = {}

        # Extract title
        title_elem = soup.find('h1', class_='title')
        if title_elem:
            title = title_elem.get_text(strip=True)
            # Remove "Title:" prefix
            title = re.sub(r'^Title:\s*', '', title)
            info['title'] = title

        # Extract authors
        authors_elem = soup.find('div', class_='authors')
        if authors_elem:
            authors = authors_elem.get_text(strip=True)
            # Remove "Authors:" prefix
            authors = re.sub(r'^Authors:\s*', '', authors)
            info['authors'] = authors

        # Extract abstract
        abstract_elem = soup.find('blockquote', class_='abstract')
        if abstract_elem:
            abstract = abstract_elem.get_text(strip=True)
            # Remove "Abstract:" prefix
            abstract = re.sub(r'^Abstract\s*', '', abstract)
            info['abstract'] = abstract

        # Extract subjects
        subjects_elem = soup.find('td', class_='tablecell subjects')
        if subjects_elem:
            info['subjects'] = subjects_elem.get_text(strip=True)

        return info

    def _download_pdf(self, paper_id: str) -> Optional[Path]:
        """Download arXiv PDF"""
        pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"

        # Use /pdf/{id} without .pdf for arXiv
        if not paper_id.endswith('.pdf'):
            pdf_url = f"https://arxiv.org/pdf/{paper_id}"

        response = self._get(pdf_url, stream=True)
        if response.status_code != 200:
            print(f"Failed to download PDF: {response.status_code}")
            return None

        # Save PDF
        pdf_dir = Path(STORAGE_BASE) / 'academic' / 'pdfs'
        pdf_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = pdf_dir / f"{paper_id}.pdf"

        with open(pdf_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return pdf_path

    def _parse_pdf(self, pdf_path: Path) -> str:
        """Parse PDF content using PyMuPDF"""
        if not pdf_path or not pdf_path.exists():
            return ''

        try:
            import fitz
            doc = fitz.open(str(pdf_path))
            text = ''

            for page in doc:
                text += page.get_text()

            doc.close()
            return text

        except ImportError:
            print("PyMuPDF not installed, skipping PDF parsing")
            return ''
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return ''

    def _translate_content(self, content: str, max_chunk: int = 3000) -> str:
        """
        Translate paper content in chunks.

        Args:
            content: Full paper text
            max_chunk: Maximum characters per chunk

        Returns:
            Translated content
        """
        if not content:
            return ''

        # Split into paragraphs
        paragraphs = content.split('\n\n')
        translated_paragraphs = []

        current_chunk = ''
        for para in paragraphs:
            if len(current_chunk) + len(para) > max_chunk:
                # Translate current chunk
                if current_chunk.strip():
                    t = self.translator.translate(current_chunk)
                    translated_paragraphs.append(t)
                    time.sleep(self.delay)

                current_chunk = para
            else:
                current_chunk += '\n\n' + para

        # Translate remaining
        if current_chunk.strip():
            t = self.translator.translate(current_chunk)
            translated_paragraphs.append(t)

        return '\n\n'.join(translated_paragraphs)

    def format_as_markdown(self, paper_data: Dict) -> str:
        """
        Format paper as markdown.

        Args:
            paper_data: Paper data from fetch_paper

        Returns:
            Formatted markdown string
        """
        metadata = paper_data.get('metadata', {})
        content = paper_data.get('content', '')

        # Translate title and abstract
        title = metadata.get('title', paper_data['paper_id'])
        translated_title = self.translator.translate(title)

        md = format_markdown_frontmatter(
            title=translated_title,
            source='arxiv.org',
            url=paper_data['abs_url'],
            date=datetime.now().strftime('%Y-%m-%d'),
            category=f"academic/arxiv/{paper_data['category']}",
            translated=True,
            fetched_at=get_file_timestamp(),
            paper_id=paper_data['paper_id'],
            pdf_url=paper_data['pdf_url'],
            authors=metadata.get('authors', ''),
        )

        md += f"# {translated_title}\n\n"

        if metadata.get('authors'):
            md += f"**作者**: {metadata['authors']}\n\n"

        if metadata.get('subjects'):
            md += f"**分类**: {metadata['subjects']}\n\n"

        if metadata.get('abstract'):
            md += "---\n\n## 摘要\n\n"
            abstract_translated = self.translator.translate(metadata['abstract'])
            md += f"{abstract_translated}\n\n"

        if content:
            md += "---\n\n## 正文\n\n"
            md += content
            md += "\n\n"

        md += f"*原文请访问 [arXiv]({paper_data['abs_url']}) | [PDF下载]({paper_data['pdf_url']})*\n"

        return md


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Fetch academic papers')
    parser.add_argument('--paper_id', type=str, help='Specific paper ID (e.g., 2606.20527)')
    parser.add_argument('--url', type=str, help='Paper URL')
    parser.add_argument('--category', type=str, default='cs.CL', help='Paper category')
    parser.add_argument('--list_url', type=str, help='Fetch from arXiv list URL')

    args = parser.parse_args()

    fetcher = AcademicFetcher()

    if args.paper_id:
        # Fetch specific paper
        print(f"Fetching paper {args.paper_id}...")
        try:
            result = fetcher.fetch_paper(args.paper_id, args.category)
            md = fetcher.format_as_markdown(result)

            # Save
            output_dir = Path(STORAGE_BASE) / 'academic' / 'arxiv' / args.category
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{args.paper_id}.md"
            output_file.write_text(md, encoding='utf-8')

            print(f"Saved to {output_file}")

        except Exception as e:
            print(f"Error: {e}")

    elif args.url:
        # Extract paper_id from URL and fetch
        paper_id = parse_arxiv_id(args.url)
        if paper_id:
            print(f"Fetching paper {paper_id}...")
            try:
                result = fetcher.fetch_paper(paper_id, args.category)
                md = fetcher.format_as_markdown(result)

                output_dir = Path(STORAGE_BASE) / 'academic' / 'arxiv' / args.category
                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = output_dir / f"{paper_id}.md"
                output_file.write_text(md, encoding='utf-8')

                print(f"Saved to {output_file}")

            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Could not extract paper ID from URL: {args.url}")

    elif args.list_url:
        # Fetch paper list
        print(f"Fetching paper list from {args.list_url}...")
        try:
            papers = fetcher.fetch_arxiv_list(args.list_url)
            print(f"Found {len(papers)} papers")

            for paper in papers[:5]:  # Limit to 5 for demo
                print(f"  - {paper['paper_id']}: {paper['title'][:50]}...")

        except Exception as e:
            print(f"Error: {e}")

    else:
        print("Fetching recent arXiv papers...")
        # Fetch recent cs.CL papers as demo
        url = "https://arxiv.org/list/cs.CL/recent"
        try:
            papers = fetcher.fetch_arxiv_list(url)
            print(f"Found {len(papers)} papers")

            # Show first 5
            for paper in papers[:5]:
                print(f"\n{paper['paper_id']}: {paper['title'][:60]}...")
                print(f"  Authors: {paper['authors'][:100]}...")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
