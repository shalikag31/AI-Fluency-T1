"""Tools the agent is allowed to use."""
import ast
import operator
from config import COURSE_FEES

def get_course_fee(course_code: str) -> str:
    fee = COURSE_FEES.get(course_code.strip().upper())
    return str(fee) if fee is not None else f"Unknown course code: {course_code}"

# Safe calculator (never use eval)
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}

def evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        return OPS[type(node.op)](evaluate(node.left), evaluate(node.right))

    if isinstance(node, ast.UnaryOp):
        return OPS[type(node.op)](evaluate(node.operand))

    raise ValueError("Unsupported expression")

def calculator(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode="eval")
        return str(evaluate(tree.body))
    except Exception as e:
        return f"Calculator error: {e}"

TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee,
    "calculator": calculator,
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get fee of one course.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {"type": "string"}
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }
    }
]

if __name__ == "__main__":
    print(get_course_fee("AI202"))
    print(calculator("(12000+18000)*0.9"))
    print(calculator("15000-12000"))