from models.message import Message


class Conversation:
    def __init__(self, max_history: int = 10):
        self.messages = []
        self.max_history = max_history

    def add_message(self, role: str, content: str):
        msg = Message(role, content)
        self.messages.append(msg)

        if len(self.messages) > self.max_history:
            self.messages.pop(0)

    def get_history(self):
        return [m.to_dict() for m in self.messages]

    def clear(self):
        self.messages = []

    def display(self):
        for msg in self.messages:
            print(f"{msg.role.upper()}: {msg.content}")



""" from models.message import Message
— Brings in the Message class we just built so Conversation can use it

self.messages = []
— Starts with an empty list, this is where all messages get stored

max_history = 10
— Only keeps the last 10 messages so the AI doesn't get overwhelmed with too much history

add_message()
— Creates a new Message object and adds it to the list. If the list gets bigger than 10 it removes the oldest one

get_history()
— Returns all messages as dictionaries, this is what gets sent to the AI API

clear()
— Wipes the conversation clean, like starting a new chat

display()
— Prints the conversation in a readable way so we can test it in the terminal"""