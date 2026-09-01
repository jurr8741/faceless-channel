import os
import requests

def generate_voice():
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Standaard stem (Rachel), pas aan naar wens
    
    with open("assets/story.txt", "r", encoding="utf-8") as f:
        text = f.read()

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(url, json=data, headers=headers)
    
    os.makedirs("assets", exist_ok=True)
    with open("assets/voiceover.mp3", "wb") as f:
        f.write(response.content)
        
    print("Voice-over gegenereerd!")

if __name__ == "__main__":
    generate_voice()
