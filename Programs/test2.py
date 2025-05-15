from openai import OpenAI
client = OpenAI(api_key = "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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
