# app/chat.py
from typing import List
from app.prompts import generate_questions
from app.utils import sanitize_input

class ChatSession:
    """
    ChatSession stores candidate info and chat history.
    It can generate technical questions (offline) using prompts.generate_questions.
    """
    def __init__(self):
        self.candidate_info = {}
        self.chat_history = []

    def greet_candidate(self) -> str:
        return "Hello! Welcome to TalentScout Hiring Assistant. I will guide you through the initial screening process."

    def end_conversation(self) -> str:
        return "Thank you for your time! We will review your responses and get back to you soon."

    def collect_info(self, field: str, value):
        """Sanitize and store a single field."""
        self.candidate_info[field] = sanitize_input(value)
        return f"{field} recorded."

    def generate_technical_questions(self, tech_stack: List[str]) -> List[str]:
        """
        For each tech in tech_stack, call generate_questions() which returns
        a list of questions (3) for that tech. Returns flattened list.
        """
        questions_out = []
        for tech in tech_stack:
            tech_clean = sanitize_input(tech)
            if not tech_clean:
                continue
            qs = generate_questions(tech_clean)
            # Prefix questions with tech name for clarity
            for q in qs:
                questions_out.append(f"[{tech_clean}] {q}")
        return questions_out
