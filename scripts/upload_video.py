import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    raw_token = os.environ.get("YOUTUBE_TOKEN")
    if not raw_token:
        raise ValueError("YOUTUBE_TOKEN is niet ingesteld!")

    # Strip eventuele lege ruimtes of newline tekens
    raw_token = raw_token.strip()
    
    token_data = json.loads(raw_token)
    
    credentials = Credentials.from_authorized_user_info(token_data)
    youtube = build("youtube", "v3", credentials=credentials)

    file_path = "assets/output.mp4"
    
    body = {
        "snippet": {
            "title": "A Romance Story #Shorts",
            "description": "Daily romance story. Subscribe for more! #romance #stories #shorts",
            "tags": ["romance", "story", "shorts"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype="video/mp4")
    
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )
    
    response = request.execute()
    print(f"Video succesvol geüpload! Video ID: {response.get('id')}")

if __name__ == "__main__":
    upload_video()
