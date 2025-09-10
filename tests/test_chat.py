# tests/test_chat.py
import unittest
from app.chat import ChatSession

class TestChatSession(unittest.TestCase):
    def test_collect_info(self):
        session = ChatSession()
        session.collect_info("Name", "Alice")
        self.assertEqual(session.candidate_info["Name"], "Alice")

    def test_generate_questions_empty(self):
        session = ChatSession()
        qs = session.generate_technical_questions([])
        self.assertEqual(qs, [])

    def test_generate_questions_known_tech(self):
        session = ChatSession()
        qs = session.generate_technical_questions(["Python"])
        self.assertTrue(len(qs) >= 1)
        self.assertIn("python", qs[0].lower())  # the prefix contains the tech name
