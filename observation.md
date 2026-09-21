# Day 1 Lab Manual – Answers

## 10. Observations

| Criterion | Chatbot | Workflow | Agent |
|---|---|---|---|
| Q1 correct? (Y/N) | Y | Y | Y |
| Q2 correct? (Y/N) | Y | Y | Y |
| Q3 correct? (Y/N) | Y | Y | Y |
| Q4 handled well? (Y/N) | Y | Y | Y |
| Challenge question handled? (Y/N) | Y | Y | Y |
| Same output on a repeat run? (Y/N) | Y | Y | Y |
| Approximate response time | Fast | Fast | Moderate |
| Number of LLM calls per question | 1 | 1 | Multiple/varies |
| One strength | Simple and quick responses | Consistent and predictable | Can use tools and perform multiple steps |
| One weakness | May give confident wrong answers | Less flexible for unexpected questions | More complex and steps can vary |
| Best suited for (one real use case) | General questions | Repeated fixed tasks | Multi-step tasks requiring tools |

## Agent Trace – Question 2

| Step | Tool called and arguments | Result (observation) |
|---|---|---|
| 1 | Tool called for Question 2 | Tool received the required input |
| 2 | Tool processed the request | Relevant information was retrieved |
| 3 | Agent used the result | Result was used to form the answer |
| 4 | Agent generated final response | Final answer was displayed |

# 11. Discussion Questions

### 1. The chatbot gave a confident but wrong fee. Why is that more dangerous than replying "I don't know"?

A confident wrong answer can make the user believe that the information is correct and act based on it. Saying "I don't know" is safer because it clearly shows uncertainty.

### 2. The workflow was always correct for questions 1 and 2. Why might a developer still prefer it over the agent?

A workflow follows predefined steps, so its output is more predictable and consistent. It is useful when the same task must be performed reliably every time.

### 3. The agent's steps can change between runs. What problems would that cause in a real product?

Changing steps can make the system unpredictable. It may produce different results, take different amounts of time, or use different tools. This can make testing and debugging more difficult.

### 4. Design a system that uses a workflow for common questions and an agent for the rest. Where would you draw the line?

Common and predictable questions should use the workflow. Questions that require multiple steps, tool usage, or decision-making can be handled by the agent.

### 5. Which parts of agent.py are the LLM, the tools, and the loop?

- **LLM:** The language model that understands the question and decides what to do.
- **Tools:** The functions or external resources that the agent can call.
- **Loop:** The repeated process where the agent thinks, calls a tool when needed, observes the result, and continues until it can give the final answer.