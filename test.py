import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="You: Comment vas-tu ?",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

print(response['choices'][0]['text'].replace('\n\n', ''))