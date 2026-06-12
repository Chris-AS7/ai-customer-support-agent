import os
from dotenv import load_dotenv
from models.conversation import Conversation
from services.prompt_builder import PromptBuilder
from services.guardrails import Guardrails
from services.llm_client import LLMClient

# Load API key from .env file
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# Our fake product knowledge base
docs = """
- To reset your password, click Forgot Password on the login page.
- If you don't receive the reset email, check your spam folder.
- To cancel your subscription, go to Settings then Billing then Cancel.
- Refunds are processed within 5-7 business days.
- Customer support is available Monday to Friday 9am to 5pm EST.
- To update your email address, go to Settings then Profile.
"""

# Set up our components
chat = Conversation()
prompt_builder = PromptBuilder(company_name="TechCorp", docs=docs)
guardrails = Guardrails(allowed_topics=[
    "password", "email", "subscription",
    "refund", "cancel", "support", "billing"
])
llm = LLMClient(api_key=api_key)

# Build the system prompt
system_prompt = prompt_builder.build_system_prompt()

print("=== TechCorp Support Agent ===")
print("Type your question or type 'quit' to exit\n")

# Chat loop
while True:
    user_input = input("YOU: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if not guardrails.is_on_topic(user_input):
        print(f"AGENT: {guardrails.off_topic_response()}\n")
        continue

    chat.add_message("user", user_input)

    response = llm.get_response(system_prompt, chat.get_history())

    chat.add_message("assistant", response)

    print(f"AGENT: {response}\n")