import os
from openai import OpenAI

def generate_story():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = "Schrijf een korte, meeslepende en chaotische anekdote van maximaal 100 woorden over iemand die op een hele vreemde manier zijn zonnebril kwijtraakt of sloopt."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    story = response.choices[0].message.content.strip()
    
    os.makedirs("assets", exist_ok=True)
    with open("assets/story.txt", "w", encoding="utf-8") as f:
        f.write(story)
        
    print("Verhaal gegenereerd!")
    return story

if __name__ == "__main__":
    generate_story()
