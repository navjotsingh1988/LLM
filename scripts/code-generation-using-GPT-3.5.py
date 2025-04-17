# Import os package. It is required to access operating system resources
import os
# OpenAI module is used for accessing the OpenAI API.
from openai import OpenAI

# Import OpenAI client and initialize with your API key.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# AI Code Generator Agent
# ------------------------
# Given a list of problem statements, this agent automatically writes
# Python code solutions for each.

problem_statements = [
    "sum of two numbers",
    "sum of unique elements",
    "longest palindrome",
    "all possible permutations of a string",
]

# set the behavior of an AI assistant i.e ChatGPT, by assigning it a role.
# "role": "system" --> means it's an instruction to the AI on how it should behave.
# "content": "You are a computer programmer" tells the AI to act like a programmer.

chat = [
    {
        "role": "system",
        "content": "You are a computer programmer"
    }
]

# instructing the assistant to generate Python code
prefix = "Write Python code for finding the "
for problem in problem_statements:
    # keep chat as the original system prompt and use chat_history to track the full interaction
    chat_history = chat.copy()

    # "role": "user" tells the model this message is from the user. "content" is the actual message text.
    chat_history.append(
        {
            "role": "user",
            "content": prefix+problem
        }
    )

    # OpenAI Python SDK (v1) to interact with ChatGPT models
    reply = client.chat.completions.create(
        model = "gpt-3.5-turbo-1106",
        messages = chat_history
    )

    print('\n' + 'STATEMENT:' + problem.upper())
    print(reply.choices[0].message.content)
