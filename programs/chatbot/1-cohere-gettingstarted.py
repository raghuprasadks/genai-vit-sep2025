#pip install cohere python-dotenv
import cohere
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")  # Adjust path if needed

api_key = os.getenv("cohere_api_key")
#print(f"API Key: {api_key}")

co = cohere.ClientV2(api_key=api_key)

response = co.chat(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "who are you"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "I am Command, a large language model, here to help. I’ve been crafted by Cohere to provide insightful and accurate responses. How can I assist you with your query today?"
                }
            ]
        }
    ],
    temperature=0.3,
    model="command-a-03-2025",
)

print(response)
print(type(response))
print(dir(response))
assistant_reply = response.message.content[0].text
print(assistant_reply)
