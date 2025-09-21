import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_feedback(pr_data):
    feedback = []
    for file in pr_data["files"]:
        try:
            prompt = f"Provide feedback for this code:\n{file['content']}"
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            suggestion = response.choices[0].message.content.strip()
            feedback.append(f"AI suggestion ({file['filename']}): {suggestion}")
        except Exception as e:
            feedback.append(f"AI suggestion ({file['filename']}): Error fetching feedback")
    return feedback
