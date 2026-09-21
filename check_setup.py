import sys
from config import client, MODEL, PROVIDER

print("Python :", sys.version.split()[0])
print("Provider:", PROVIDER)
print("Model:", MODEL)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Reply with exactly: SETUP OK"}
    ],
    temperature=0,
)

print("Reply:", response.choices[0].message.content)