# app/utils.py
import re
import json
import os
from typing import Any, Dict

def sanitize_input(value: Any) -> Any:
    """
    Basic sanitization for user inputs.
    Strings are stripped; other values returned as-is.
    """
    if isinstance(value, str):
        return value.strip()
    return value

def validate_email(email: str) -> bool:
    """
    Basic email validation using a simple regex.
    """
    if not isinstance(email, str):
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email.strip()) is not None

def validate_phone(phone: str) -> bool:
    """
    Basic phone validation: digits only, length between 10 and 15.
    """
    if not isinstance(phone, str):
        return False
    s = phone.strip()
    return s.isdigit() and 10 <= len(s) <= 15

def save_candidate(candidate: Dict[str, Any], path: str = None) -> None:
    """
    Save candidate dictionary (anonymized simulated data) into data/candidates.json.
    Creates data/ directory if it doesn't exist.
    This is a simple read-modify-write (suitable for demo/small data).
    """
    if path is None:
        base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        path = os.path.join(base, "data", "candidates.json")

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Read existing
    data = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f) or []
        except Exception:
            data = []

    # Append sanitized candidate (do not write any secrets)
    to_store = candidate.copy()
    # Ensure tech stack is list of strings
    tech = to_store.get("Tech Stack", [])
    if isinstance(tech, str):
        tech = [t.strip() for t in tech.split(",") if t.strip()]
    to_store["Tech Stack"] = tech

    data.append(to_store)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
