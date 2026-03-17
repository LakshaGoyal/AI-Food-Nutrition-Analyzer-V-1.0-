import os
import json
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use latest working model
model = genai.GenerativeModel("gemini-2.5-flash")

PROMPT = """
You are an expert nutritionist.

Analyze this food image.

Identify each food item and estimate:
- calories
- protein (g)
- carbs (g)
- fat (g)

Return ONLY valid JSON in this format:

{
  "foods": [
    {
      "name": "food item",
      "calories": 0,
      "protein": 0,
      "carbs": 0,
      "fat": 0
    }
  ]
}
"""

def analyze_food_image(image_path: str):

    try:

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        img = Image.open(image_path)

        response = model.generate_content([PROMPT, img])

        if not response.candidates:
            raise ValueError("No response from Gemini")

        response_text = response.candidates[0].content.parts[0].text.strip()

        # remove markdown if present
        response_text = response_text.replace("```json", "").replace("```", "")

        data = json.loads(response_text)

        return data

    except Exception as e:
        print("Gemini Error:", e)
        return None