
import os
import openai

# IMPORTANT: For testing purposes only. In a real application,
# never hardcode API keys. Use environment variables or a secure configuration.
api_key = "xai-vY1BScFBTGI5qAyriLPaBjcpQKZfMEAzsomYlGw2gG0keQ7N6Jw9y5cVMlhSlanBsgWVt1Ip9ZPwQNdB" # REPLACE THIS WITH YOUR ACTUAL XAI_API_KEY

try:
    if not api_key or api_key == "YOUR_XAI_API_KEY":
        raise ValueError("API key not set or is placeholder. Please replace 'YOUR_XAI_API_KEY' with your actual key.")

    client = openai.OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")

    print("Making a call to Grok-4...")
    response = client.chat.completions.create(
        model="grok-4",
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ],
        temperature=0.7,
        max_tokens=50
    )

    print("Grok-4 Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
