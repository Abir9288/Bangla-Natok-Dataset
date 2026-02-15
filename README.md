🎬 Bangla Natok YouTube Dataset (Auto-Updated)

A large-scale, continuously updated dataset of Bangla Natok / Drama videos collected from YouTube using the YouTube Data API v3, designed for data science, NLP, media studies, and recommender system research.

This project automatically fetches metadata such as views, likes, comments, duration, and publishing details, and updates the dataset daily.

📌 Motivation

Bangla Natok content on YouTube represents one of the largest digital entertainment ecosystems in South Asia, yet public, structured datasets are extremely limited.

This dataset aims to support:

📊 Popularity & trend analysis

🧠 NLP & content understanding

🎭 Actor-centric analytics

🤖 Recommendation systems

📈 Engagement prediction models

📂 Dataset Overview

Each row represents one YouTube video related to Bangla Natok / Drama.

🔑 Columns
Column Name	Description
VideoID	Unique YouTube video ID
Title	Video title
Channel	Channel name
PublishDate	ISO timestamp of publication
URL	Direct YouTube link
Views	Total view count
Likes	Total likes
Comments	Total comment count
Duration_sec	Video duration (seconds)
📊 Dataset Size

Current size: 400+ videos

Daily growth: Yes (auto-updated)

Update frequency: Every 24 hours

Dataset size will continuously increase as new Bangla Natok content is published.

🔄 Automation Pipeline
YouTube API
     ↓
Python Script
     ↓
CSV Dataset
     ↓
Windows Task Scheduler (Daily)
     ↓
GitHub / Kaggle

⚙️ Data Collection Method

API: YouTube Data API v3

Search Queries:

"Bangla Natok"

"Bangla Drama"

Pagination: Handled via nextPageToken

Rate-limit safe: Uses delays between requests

🧪 Technologies Used

Python 3.10+

google-api-python-client

pandas

isodate

tqdm

Windows Task Scheduler

Git & GitHub

Kaggle API

🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/Abir9288/Bangla-Natok-Dataset.git
cd Bangla-Natok-Dataset

2️⃣ Install Dependencies
pip install google-api-python-client pandas isodate tqdm kaggle

3️⃣ Add Kaggle API Token

Place kaggle.json in:

C:\Users\<YourUsername>\.kaggle\

4️⃣ Run Update Script
python update_dataset.py

⏰ Daily Auto-Update (Windows)

This project uses Windows Task Scheduler to run:

python update_dataset.py


Trigger: Daily

Action: Start Python script

Ensures dataset stays current without manual work

📦 Kaggle Dataset

This dataset is designed for direct Kaggle publishing and versioning.

✔ Clean CSV

✔ Reproducible pipeline

✔ Daily updates

✔ Research-ready

Kaggle upload is handled automatically using the Kaggle API.

🔐 Security & Ethics

No private or personal user data collected

Only publicly available metadata is used

API keys are excluded via .gitignore

Fully compliant with YouTube API Terms of Service

🧠 Future Enhancements

Planned improvements:

🎭 Actor name detection (NLP)

💬 Comment sentiment analysis

📈 Engagement score modeling

🧠 Topic modeling on titles

🤖 Recommendation baseline models

📜 License

This dataset is released under the MIT License.
You are free to use, modify, and distribute with attribution.

👤 Author

Abir
Data Science & Machine Learning Enthusiast
🇧🇩 Bangladesh

GitHub: https://github.com/Abir9288
