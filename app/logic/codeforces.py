import requests

def scrape_codeforces_problems(limit=200):
    url = "https://codeforces.com/api/problemset.problems"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print("Codeforces API error:", e)
        return []

    if data["status"] != "OK":
        print("Codeforces API returned error status.")
        return []

    problems = []
    all_problems = data["result"]["problems"]

    for i, prob in enumerate(all_problems):
        if i >= limit:
            break
        problems.append({
            "title": prob.get("name"),
            "difficulty": f"level {prob.get('rating', 'N/A')}",
            "platform": "Codeforces",
            "topics": [tag.lower() for tag in prob.get("tags", [])],
            "url": f"https://codeforces.com/problemset/problem/{prob['contestId']}/{prob['index']}"
        })

    return problems
