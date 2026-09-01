import os
from moviepy.editor import AudioFileClip, ColorClip, CompositeVideoClip, TextClip

def build_video():
    audio = AudioFileClip("assets/voiceover.mp3")
    
    # Maak een simpele zwarte/donkere achtergrond op Shorts-formaat (1080x1920)
    background = ColorClip(size=(1080, 1920), color=(15, 15, 15), duration=audio.duration)
    
    video = background.set_audio(audio)
    
    os.makedirs("assets/output", exist_ok=True)
    output_path = "assets/output/final_video.mp4"
    video.write_videofile(output_path, fps=30, codec="libx264", audio_codec="aac")
    print(f"Video opgeslagen op {output_path}")

if __name__ == "__main__":
    build_video()
