import openai

def get_ai_feedback(file_content, openai_api_key):
    openai.api_key = openai_api_key
    prompt = f"Review this Python code and suggest improvements:\n\n{file_content}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
