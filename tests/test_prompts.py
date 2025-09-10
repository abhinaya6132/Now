# tests/test_prompts.py
import unittest
from app.prompts import generate_questions

class TestPrompts(unittest.TestCase):
    def test_generate_python_questions(self):
        qs = generate_questions("Python")
        self.assertEqual(len(qs), 3)
        self.assertTrue(any("python" in q.lower() or "list" in q.lower() for q in qs))
