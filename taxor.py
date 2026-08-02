import os
import json
import base64

# Import the official SDKs
from google import genai
from google.genai import types
client = genai.Client(api_key="")
# from openai import OpenAI
# from anthropic import Anthropic

# ==========================================
# CONFIGURATION & PROMPTS
# ==========================================

SYSTEM_PROMPT = """
You are a highly accurate OCR and data extraction assistant specialized in reading handwritten Indian bills and receipts. 
Your task is to extract key billing information from the provided image and output it STRICTLY as a valid JSON object matching the schema below. 
If a specific field is illegible or missing from the receipt, return null for that field. Do not include markdown formatting, backticks, or any conversational text.

Required JSON Schema:
{
  "vendor_name": "string or null",
  "date": "YYYY-MM-DD or null",
  "total_amount": float or null,
  "tax_amount": float or null,
  "line_items": [
    {
      "description": "string",
      "amount": float
    }
  ]
}
"""

def encode_image(image_path):
    """Encodes an image to base64 for API transmission."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def read_image_bytes(image_path):
    """Reads raw bytes (specifically for the new Google GenAI SDK)."""
    with open(image_path, "rb") as image_file:
        return image_file.read()

# ==========================================
# MODEL WRAPPERS
# ==========================================

def extract_with_gemini(image_path):
    """Calls Gemini 2.5 Flash using the google-genai SDK."""
    print("Sending to Gemini 2.5 Flash...")
    
    image_bytes = read_image_bytes(image_path)
    
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=[
            SYSTEM_PROMPT,
            types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )
    return json.loads(response.text)


if __name__ == "__main__":
    # Replace with the path to your test receipt image
    test_image = "digital_01.jpeg"
    
    if not os.path.exists(test_image):
        print(f"Error: {test_image} not found. Please add a test image to the directory.")
        exit(1)

    try:
        gemini_result = extract_with_gemini(test_image)
        print("\n--- Gemini Result ---")
        print(json.dumps(gemini_result, indent=2))
    except Exception as e:
        print(f"Gemini Error: {e}")
