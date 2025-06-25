import requests
import json

def scrape_leetcode_problems(limit=100):
    url = "https://leetcode.com/graphql"
    query = """
    query questionList($limit: Int, $skip: Int) {
      problemsetQuestionList: questionList(
        categorySlug: ""
        limit: $limit
        skip: $skip
      ) {
        questions {
          title
          titleSlug
          difficulty
          topicTags {
            name
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
        payload = {
            "query": query,
            "variables": {"limit": batch_size, "skip": skip}
        }

        response = requests.post(url, json=payload, headers=headers)

        try:
            data = response.json()
        except Exception as e:
            print("Failed to parse JSON response:", e)
            print("Response content:\n", response.text)
            return

        if "data" not in data or "problemsetQuestionList" not in data["data"]:
            print("Unexpected response structure. Full response:\n", json.dumps(data, indent=2))
            return

        questions = data["data"]["problemsetQuestionList"]["questions"]

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

    with open("app/data/leetcode_problems.json", "w") as f:
        json.dump(problems[:limit], f, indent=2)

    print(f"Scraped {len(problems[:limit])} problems from LeetCode.")


if __name__ == "__main__":
    scrape_leetcode_problems(limit=200)
