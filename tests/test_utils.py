# tests/test_utils.py
import unittest
from app.utils import sanitize_input, validate_email, validate_phone, save_candidate
import os
import json
import tempfile

class TestUtils(unittest.TestCase):
    def test_sanitize_input(self):
        self.assertEqual(sanitize_input("  hello "), "hello")
    
    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("bad-email"))
    
    def test_validate_phone(self):
        self.assertTrue(validate_phone("9876543210"))
        self.assertFalse(validate_phone("123abc"))

    def test_save_candidate_creates_file(self):
        # use a temp file path
        tmpdir = tempfile.mkdtemp()
        path = os.path.join(tmpdir, "candidates.json")
        candidate = {
            "Name": "T",
            "Email": "t@example.com",
            "Phone": "9876543210",
            "Experience": 1,
            "Position": "Dev",
            "Location": "City",
            "Tech Stack": ["Python"]
        }
        save_candidate(candidate, path=path)
        self.assertTrue(os.path.exists(path))
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, list)
        self.assertEqual(data[-1]["Email"], "t@example.com")
