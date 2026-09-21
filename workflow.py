import re
from config import COURSE_FEES, QUESTIONS

def workflow(question):
    codes = re.findall(r"[A-Z]{2}\d{3}", question.upper())
    fees = [COURSE_FEES[c] for c in codes if c in COURSE_FEES]

    if not fees:
        return "Sorry, I can only answer course fee questions."

    text = question.lower()

    if "total" in text:
        total = sum(fees)
        if "10%" in text:
            total *= 0.9
        return f"Total fee: Rs. {total:,.0f}"

    if len(fees) == 1:
        return f"Fee for {codes[0]}: Rs. {fees[0]:,}"

    return "No matching rule."

print("\n=== SYSTEM 2 ===\n")

for q in QUESTIONS:
    print("Q:", q)
    print("A:", workflow(q))
    print("-" * 60)