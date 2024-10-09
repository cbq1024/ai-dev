import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)