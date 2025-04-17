# accessing operating system resources
import os
# accessing the OpenAI API
from openai import OpenAI

# Import OpenAI client and initialize with your API key.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# AI Text Summary Generator Agent
# ------------------------
# Given a text, it will provide the Summary

text = """
The beloved sitcom Friends centers around six main characters living in New York
City, each with their own distinct personality and charm. Rachel Green starts
off as a spoiled runaway bride but grows into a confident fashion executive.
Monica Geller, a chef and Rachel’s former high school friend, is known for her
obsessive cleanliness and competitive nature. Her brother, Ross Geller, is a
paleontologist whose multiple divorces and awkward demeanor become a recurring
joke. Phoebe Buffay, the quirky masseuse and musician, adds eccentric humor with
her offbeat songs and backstory. Chandler Bing is the sarcastic joker of the
group, often using humor to deflect his insecurities, and he eventually finds
love and maturity through his relationship with Monica. Joey Tribbiani, the
aspiring actor with a big heart and a small attention span, brings warmth and
comic relief with his lovable goofiness and memorable catchphrase, “How you
doin’?” Together, their friendships, love lives, and personal growth make
Friends a timeless series that continues to resonate with audiences around
the world.
"""

# set the behavior of an AI assistant i.e ChatGPT, by assigning it a role.
chat = [
    {
        "role": "system",
        "content": "You are a experienced content writer"
    }
]

# instructing the assistant to generate summary
suffix = "\nSummarize the above text in 100 words:\n"
query = text + suffix

# "role": "user" tells the model this message is from the user.
# "content" is the actual message text.
chat.append(
    {
        "role": "user",
        "content": query
    }
)

# OpenAI Python SDK (v1) to interact with ChatGPT models
reply_from_model = client.chat.completions.create(
    model = "gpt-3.5-turbo-1106",
    messages = chat
)

# Text Summary
print(reply_from_model.choices[0].message.content)
