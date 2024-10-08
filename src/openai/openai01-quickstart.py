import openai
import os

openai.api_key = os.environ['EPHONE_AI_KEY']
openai.base_url  = os.environ['EPHONE_AI_URL']
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion)