from scripts.generate_story import generate_story
from scripts.generate_voice import generate_voice
from scripts.build_video import build_video
from scripts.upload_video import upload_video

def main():
    print("--- Start Faceless Channel Pipeline ---")
    generate_story()
    generate_voice()
    build_video()
    upload_video()
    print("--- Pipeline Voltooid! ---")

if __name__ == "__main__":
    main()
