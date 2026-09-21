from config import client, MODEL, QUESTIONS, banner

def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful college assistant."},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    return response.choices[0].message.content

banner("SYSTEM 1")

for q in QUESTIONS:
    print("Q:", q)
    print("A:", chatbot(q))
    print("-" * 60)