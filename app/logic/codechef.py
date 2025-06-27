# codechef.py
import requests
from bs4 import BeautifulSoup

def scrape_codechef_problems(limit=100):
    url = "https://www.codechef.com/problems/school"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    problems = []
    rows = soup.select("tbody tr")

    for i, row in enumerate(rows):
        if i >= limit:
            break
        cols = row.find_all("td")
        if len(cols) < 2:
            continue
        title = cols[1].text.strip()
        link = "https://www.codechef.com" + cols[1].find("a")["href"]
        problems.append({
            "title": title,
            "difficulty": "school",
            "platform": "CodeChef",
            "topics": [],
            "url": link
        })

    print(f"✅ Total Codechef problems scraped: {len(problems)}")
    return problems
