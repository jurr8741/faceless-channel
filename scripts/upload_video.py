import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    # In GitHub Actions lezen we de JSON direct uit de Secret environment variables
    if os.environ.get("YOUTUBE_TOKEN"):
        token_data = json.loads(os.environ.get("YOUTUBE_TOKEN"))
        creds = Credentials.from_authorized_user_info(token_data)
    else:
        creds = Credentials.from_authorized_user_file("token.json")

    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": "Niet weer eentje! #shorts",
            "description": "Automatisch gegenereerde short.",
            "tags": ["shorts", "humor"],
            "categoryId": "23"
        },
        "status": {
            "privacyStatus": "private"  # Of 'public' zodra je het getest hebt
        }
    }

    media = MediaFileUpload("assets/output/final_video.mp4", chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    
    response = request.execute()
    print(f"Video geüpload! Video ID: {response.get('id')}")

if __name__ == "__main__":
