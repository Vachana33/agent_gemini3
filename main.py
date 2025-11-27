# main.py
from dotenv import load_dotenv
load_dotenv()


from agent import Agent
from tools import file_tools

agent = Agent(
    model="gemini-3-pro-preview",
    tools=file_tools,
    system_instruction="You are a helpful Coding Assistant. Respond like you are Linus Torvalds."
)

print("Agent ready. Ask it to check files in this directory.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break

    response = agent.run(user_input)
    print(f"Linus: {response.text}\n")
