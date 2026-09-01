import os
import requests

def generate_voice():
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY is niet ingesteld!")

    with open("assets/story.txt", "r", encoding="utf-8") as f:
        text = f.read()

    voice_id = "pNInz6obpgDQGcFmaJgB"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        raise RuntimeError(f"ElevenLabs API fout ({response.status_code}): {response.text}")

    os.makedirs("assets", exist_ok=True)
    with open("assets/voiceover.mp3", "wb") as f:
        f.write(response.content)

    print("Voice-over succesvol gegenereerd!")

if __name__ == "__main__":
    generate_voice()
