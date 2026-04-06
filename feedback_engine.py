import os
from dotenv import load_dotenv
from groq import Groq
from prompts import RESUME_FEEDBACK_PROMPT

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_feedback(resume_text):
    """
    Sends resume text to LLaMA and returns structured feedback.
    """

    prompt = RESUME_FEEDBACK_PROMPT.format(
        resume_text=resume_text
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical recruiter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=800
    )

    return response.choices[0].message.content