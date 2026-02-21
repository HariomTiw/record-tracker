import os
import json
from urllib import response
from dotenv import load_dotenv
from PIL import Image
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def validate_records(data):
    cleaned = []

    for r in data.get("records", []):
        try:
            cleaned.append({
                "sr_no": int(r["sr_no"]),
                "name": str(r["name"]).strip(),
                "morning": 1 if r["morning"] == 1 else 0,
                "afternoon": 1 if r["afternoon"] == 1 else 0,
                "night": 1 if r["night"] == 1 else 0
            })
        except Exception:
            print("Skipping bad record:", r)

    return {
        "date": data.get("date"),
        "records": cleaned
    }

def extract_meal_data(image_path):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    prompt = """
    Return ONLY valid JSON.
    Do NOT add explanation.
    Do NOT add comments.
    Do NOT change key names.
    Use exactly these keys:

    {
    "records": [
        {
        "sr_no": integer,
        "name": string,
        "morning": 0 or 1,
        "afternoon": 0 or 1,
        "night": 0 or 1
        }
    ],
    "date": "YYYY-MM-DD"
    }

    Do not misspell keys.
    Do not rename fields.
    Do not include extra spaces inside keys.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {"text": prompt},
            {
                "inline_data": {
                    "mime_type": "image/jpg",
                    "data": image_bytes
                }
            }
        ],
        config={
            "response_mime_type": "application/json",
            "response_schema": {
                "type": "object",
                "properties": {
                    "date": {"type": "string"},
                    "records": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "sr_no": {"type": "integer"},
                                "name": {"type": "string"},
                                "morning": {"type": "string","enum": ["0", "1"]},
                                "afternoon": {"type": "string","enum": ["0", "1"]},
                                "night": {"type": "string","enum": ["0", "1"]}

                            },
                            "required": ["sr_no", "name", "morning", "afternoon", "night"]
                        }
                    }
                },
                "required": ["date", "records"]
            }
        }
    )

    data = response.parsed
    return validate_records(data)
