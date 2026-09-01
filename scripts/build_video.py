import os
from moviepy import AudioFileClip, ColorClip, CompositeVideoClip, TextClip

def build_video():
    audio = AudioFileClip("assets/voiceover.mp3")
    duration = audio.duration

    # Achtergrond maken
    background = ColorClip(size=(1080, 1920), color=(15, 15, 25), duration=duration)
    
    # Audio koppelen via MoviePy v2 syntaxis
    video = background.with_audio(audio)

    os.makedirs("assets", exist_ok=True)
    video.write_videofile(
        "assets/output.mp4",
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )

    audio.close()
    video.close()
    print("Video succesvol gegenereerd!")

if __name__ == "__main__":
    build_video()
