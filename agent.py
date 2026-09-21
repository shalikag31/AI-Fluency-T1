"""System 3: AI Agent"""
import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS

SYSTEM_PROMPT = """
You are a college fee assistant.

Rules:
1. Never guess course fees.
2. Always use get_course_fee for fee questions.
3. Use calculator for calculations.
4. Course codes: CS101, AI202, DS303.
"""

def agent(question):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0,
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            return msg.content

        messages.append(msg)

        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments)

            result = TOOL_FUNCTIONS[name](**args)

            print(f"Tool → {name} {args} = {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            })

if __name__ == "__main__":
    banner("SYSTEM 3 : AI AGENT")

    for q in QUESTIONS:
        print("Q:", q)
        print("A:", agent(q))
        print("-" * 60)