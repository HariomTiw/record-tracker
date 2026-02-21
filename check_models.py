import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("--- Available Models ---")
try:
    # The correct method is .list()
    for m in client.models.list():
        # print the model name (e.g., 'models/gemini-2.0-flash')
        print(m.name)
except Exception as e:
    print(f"Error: {e}")