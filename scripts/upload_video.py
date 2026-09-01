import os
import json
import re
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    raw_token = os.environ.get("YOUTUBE_TOKEN")
    if not raw_token:
        raise ValueError("YOUTUBE_TOKEN is niet ingesteld!")

    # Zoek het eerste geldige JSON object {...} op in de string
    match = re.search(r'\{.*?\}', raw_token, re.DOTALL)
    if not match:
        raise ValueError("Geen geldige JSON structuur gevonden in YOUTUBE_TOKEN!")

    clean_json_str = match.group(0)

    try:
        token_data = json.loads(clean_json_str)
    except json.JSONDecodeError as e:
        print("FOUT bij het parseren van YOUTUBE_TOKEN:")
        print(clean_json_str)
        raise e

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
