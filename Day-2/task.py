%pip install groq
from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")

print("Groq API key loaded successfully!")

%%writefile day2_recraft_ai_assistant.py

import json
import functools
import os
from groq import Groq

# Connect to Groq API
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-20b"

# ReCraft AI Business Catalogue
CATALOGUE = {
    "plastic bottles": "Can be converted into planters",
    "old paper": "Can be recycled into paper products",
    "cardboard": "Can be reused for storage products"
}

# System Prompt
SYSTEM = """
You are ReCraft AI, a friendly waste-to-product assistant.
Give useful recycling and upcycling suggestions.
Never invent prices or delivery dates.
Keep answers short and friendly.
"""

# Decorator
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper

# Product information function
@log_call
def get_product_info(item: str) -> str:
    """Return product information from the ReCraft catalogue."""
    return CATALOGUE.get(
        item.lower().strip(),
        "Information not available."
    )

# Few-shot message classification
def classify_message(message: str) -> str:
    """Classify a customer message using few-shot examples."""

    examples = [
        {"role": "system", "content":
         "Classify messages as product_idea, how_to or other. "
         "Return only the category."},
        {"role": "user", "content": "Give me recycling ideas"},
        {"role": "assistant", "content": "product_idea"},
        {"role": "user", "content": "How to recycle paper?"},
        {"role": "assistant", "content": "how_to"},
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=examples
    )

    return response.choices[0].message.content.strip()

# JSON example
def create_customer_data(name: str, material: str) -> dict:
    """Create structured customer data."""
    data = {
        "name": name,
        "waste_material": material
    }
    return json.loads(json.dumps(data))

# Chat memory
history = [{"role": "system", "content": SYSTEM}]

def chat(user_text: str) -> str:
    """Maintain conversation history and generate a Groq AI response."""

    history.append({"role": "user", "content": user_text})

    recent = [history[0]] + history[1:][-8:]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent
        )
        reply = response.choices[0].message.content

    except Exception as error:
        reply = f"Groq API error: {error}"

    history.append({"role": "assistant", "content": reply})

    return reply

# Test the functions
print("Product Information:")
print(get_product_info("plastic bottles"))

print("\nMessage Classification:")
print(classify_message("Give me recycling ideas"))

print("\nCustomer JSON:")
print(create_customer_data("Ravi", "Plastic bottles"))

print("\nChatbot:")
print(chat("Hello!"))

print("\nDay 2 Python file created successfully!")

%run day2_recraft_ai_assistant.py
