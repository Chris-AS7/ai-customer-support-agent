class Guardrails:
    def __init__(self, allowed_topics: list):
        self.allowed_topics = allowed_topics

    def is_on_topic(self, message: str) -> bool:
        message_lower = message.lower()
        for topic in self.allowed_topics:
            if topic.lower() in message_lower:
                return True
        return False
    
    def off_topic_response(self) -> str:
        return "I can only help with questions about our products and services."
    
    
