# ✅ CORRECT
from scrape_leetcode import scrape_leetcode_problems
from codeforces import scrape_codeforces_problems
from codechef import scrape_codechef_problems
from gfg import scrape_gfg_problems

import json
import os


def save_combined_problems(leetcode_limit=100, codeforces_limit=100, codechef_limit=50, gfg_limit=50):
    print("Scraping all problems...")

    all_problems = (
        scrape_leetcode_problems(leetcode_limit)
        + scrape_codeforces_problems(codeforces_limit)
        + scrape_codechef_problems(codechef_limit)
        + scrape_gfg_problems(gfg_limit)
    )

    os.makedirs("data", exist_ok=True)
    with open("data/all_problems.json", "w") as f:
        json.dump(all_problems, f, indent=2)

    print(f"✅ Total {len(all_problems)} problems saved to data/all_problems.json")



if __name__ == "__main__":
    save_combined_problems()