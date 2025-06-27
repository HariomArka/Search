import requests
import json

def scrape_leetcode_problems(limit=200):
    print("🔍 Starting LeetCode scrape...")

    url = "https://leetcode.com/graphql"
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      questionList(
        categorySlug: $categorySlug,
        limit: $limit,
        skip: $skip,
        filters: $filters
      ) {
        totalNum
        data {
          title
          titleSlug
          difficulty
          isPaidOnly
          topicTags {
            name
            slug
          }
        }
      }
    }
    """

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/problemset/all/",
        "User-Agent": "Mozilla/5.0"
    }

    problems = []
    skip = 0
    batch_size = 50

    while len(problems) < limit:
        print(f"Fetching LeetCode batch: skip={skip}")
        payload = {
            "query": query,
            "variables": {
                "categorySlug": "",
                "skip": skip,
                "limit": batch_size,
                "filters": {}
            }
        }

        try:
            res = requests.post(url, json=payload, headers=headers, timeout=10)
            data = res.json()
            questions = data["data"]["questionList"]["data"]
        except Exception as e:
            print("❌ LeetCode error:", e)
            print("Raw response:\n", res.text if 'res' in locals() else "No response received.")
            return []

        print(f"✅ Received {len(questions)} questions")

        for q in questions:
            problems.append({
                "title": q["title"],
                "difficulty": q["difficulty"].lower(),
                "platform": "LeetCode",
                "topics": [t["name"].lower() for t in q["topicTags"]],
                "url": f"https://leetcode.com/problems/{q['titleSlug']}/"
            })

        skip += batch_size
        if not questions:
            break

    print(f"✅ Total LeetCode problems scraped: {len(problems[:limit])}")
    return problems[:limit]
