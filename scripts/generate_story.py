import os
import json
from google import genai

def generate_story():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set!")

    client = genai.Client(api_key=api_key)

    state_file = "assets/story_state.json"
    state = {"current_part": 1, "previous_story": ""}
    
    if os.path.exists(state_file):
        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)

    current_part = state.get("current_part", 1)
    previous_story = state.get("previous_story", "")

    if current_part == 1:
        prompt = (
            "Write a short, engaging romance story in English (max 350 words) for a YouTube Short. "
            "It must be unique, with varied characters, settings, and plotlines. "
            "If the story requires a continuation, end it with exact phrase: 'Come back for the next part tomorrow.' "
            "Do not include any intro, title, or extra text. Return only the story text."
        )
    else:
        continuation_instruction = (
            'If it needs one last part, end with: "Come back for the next part tomorrow."' 
            if current_part == 2 else 
            'This is the final part, wrap up the story gracefully without any cliffhanger.'
        )
        prompt = (
            f"This is Part {current_part} of an ongoing romance story (max 3 parts total).\n"
            f"Previous part: {previous_story}\n\n"
            f"Write the direct continuation of this romance story in English (max 350 words). "
            f"{continuation_instruction} "
            "Do not include any intro, title, or extra text. Return only the story text."
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    story = response.text.strip()

    has_continuation = "Come back for the next part tomorrow." in story

    if has_continuation and current_part < 3:
        next_state = {"current_part": current_part + 1, "previous_story": story}
    else:
        next_state = {"current_part": 1, "previous_story": ""}

    os.makedirs("assets", exist_ok=True)
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(next_state, f, indent=2)

    with open("assets/story.txt", "w", encoding="utf-8") as f:
        f.write(story)

    print(f"Generated Part {current_part} romance story!")
    return story

if __name__ == "__main__":
    generate_story()
