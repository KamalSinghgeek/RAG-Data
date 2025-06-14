import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def extract_text_from_url(url):
    """Fetch and clean visible text from a single page."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return ""

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    return soup.get_text(separator="\n", strip=True)


def crawl_site(base_url, max_pages=50, delay=1):
    """Crawl the site to gather text from multiple pages under the same domain."""
    visited = set()
    to_visit = [base_url]
    collected_text = []

    base_domain = urlparse(base_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        print(f"➡️ Crawling: {url}")
        text = extract_text_from_url(url)
        if text:
            collected_text.append(f"\n--- TEXT FROM: {url} ---\n\n{text}\n")
        
        # parse for internal links
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = urljoin(url, a["href"])
            if urlparse(href).netloc == base_domain and href not in visited:
                to_visit.append(href)
        
        time.sleep(delay)

    return "\n".join(collected_text)


if __name__ == "__main__":
    base_url = "https://fleetstackglobal.com/topic/We-have-a-local-server-Can-we-install-and-try"
    print("Starting crawl. This may take a while...")
    full_text = crawl_site(base_url, max_pages=30, delay=0.5)

    with open("fleetstack_forum.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    print("✅ Extraction finished!")
    print("Text saved to fleetstack_forum.txt")
