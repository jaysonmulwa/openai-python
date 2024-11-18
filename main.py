import openai

openai.api_key=""

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is an LLM anyways?"}],
    max_tokens=64
)

print(response.choices[0].message.content)


# ALTERNATIVE IMPLEMENTATION
# from openai import OpenAI
# client = OpenAI()