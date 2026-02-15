import os
import pandas as pd
from googleapiclient.discovery import build
import isodate
import time


# Set Kaggle API key location (your current folder)
os.environ["KAGGLE_USERNAME"] = "abirmdhasan"
os.environ["KAGGLE_KEY"] = "d6b2cfa2d78d041555dc417f0f4f82f2"


# CONFIG
API_KEY = "AIzaSyAiPO5HeIcBKLn8_yEqwBHgU0L_lABykiE"
QUERY = ["Bangla Natok", "Bangla Drama"]
MAX_RESULTS = 50  # number of new videos to fetch each run
CSV_FILE = "Bangla_Natok_Advanced.csv"

# Set Kaggle config directory (for automatic upload later)
os.environ["KAGGLE_CONFIG_DIR"] = os.getcwd()


# FUNCTION TO FETCH VIDEOS
def fetch_videos(query, max_results=50):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    videos = []
    next_page_token = None

    while len(videos) < max_results:
        search_request = youtube.search().list(
            q=query,
            part="id",
            type="video",
            maxResults=min(50, max_results - len(videos)),
            pageToken=next_page_token
        )
        search_response = search_request.execute()
        video_ids = [item["id"]["videoId"] for item in search_response["items"]]

        # Get video details
        details_request = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(video_ids)
        )
        details_response = details_request.execute()

        for item in details_response["items"]:
            snippet = item["snippet"]
            stats = item.get("statistics", {})
            content = item["contentDetails"]

            duration = isodate.parse_duration(content["duration"]).total_seconds()

            videos.append([
                item["id"],
                snippet["title"],
                snippet["channelTitle"],
                snippet["publishedAt"],
                f"https://youtube.com/watch?v={item['id']}",
                int(stats.get("viewCount", 0)),
                int(stats.get("likeCount", 0)),
                int(stats.get("commentCount", 0)),
                duration
            ])

        next_page_token = search_response.get("nextPageToken")
        if not next_page_token:
            break

        time.sleep(1)  # to avoid hitting YouTube API rate limits

    return videos

# =============================
# MAIN SCRIPT
# =============================

# Load existing dataset
if os.path.exists(CSV_FILE):
    df_existing = pd.read_csv(CSV_FILE)
else:
    df_existing = pd.DataFrame(columns=[
        "VideoID","Title","Channel","PublishDate","URL",
        "Views","Likes","Comments","Duration_sec"
    ])

# Fetch new videos
new_videos = fetch_videos(QUERY, MAX_RESULTS)
df_new = pd.DataFrame(new_videos, columns=df_existing.columns)

# Merge with existing data, remove duplicates
df_final = pd.concat([df_existing, df_new]).drop_duplicates(subset="VideoID", keep="last")

# Save updated CSV
df_final.to_csv(CSV_FILE, index=False)
print("Dataset updated! Total rows:", len(df_final))