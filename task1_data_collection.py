import requests
import time
import json
import os
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm",],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

collected_data = []
category_counts = {cat: 0 for cat in categories}

def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return None

# Fetch ALL top stories (not just 500)
story_ids = requests.get(TOP_STORIES_URL, headers=headers).json()
TARGET_TOTAL = 120
for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()

        if not story or "title" not in story:
            continue

        category = get_category(story["title"])

        # if category is None:
        #     continue
        if category is None:
            category = "technology"   # fallback (optional)

        # if category_counts[category] >= 25:
        #     continue
        else:
            # ✅ After category is full, still allow adding if total < TARGET
            if len(collected_data) >= TARGET_TOTAL:
                continue

        data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_data.append(data)
        category_counts[category] += 1

        # ✅ STOP ONLY when ALL categories reach 25
        if all(count >= 25 for count in category_counts.values()):
            break

    except Exception as e:
        print(f"Error fetching {story_id}: {e}")
        continue

# Save file
if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(collected_data, f, indent=4)

print(f"Collected {len(collected_data)} stories.")
print("Category counts:", category_counts)
