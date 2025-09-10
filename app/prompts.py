# app/prompts.py
"""
Offline prompt/question generator.
If you later integrate an LLM, you can replace generate_questions to call the API.
"""

from typing import List

def generate_questions(tech: str) -> List[str]:
    """
    Return 3 tailored technical questions for a given technology string.
    This is deterministic and works without an LLM.
    """
    t = tech.strip().lower()

    if "python" in t:
        return [
            "Explain list vs tuple in Python and when to use each.",
            "How does Python's garbage collector work? Explain reference counting and cycles.",
            "Write a function to remove duplicates from a list while preserving order."
        ]

    if "django" in t:
        return [
            "Describe Django's MVT pattern and how it differs from MVC.",
            "How do you create and apply migrations in Django? What is the purpose of migrations?",
            "Explain how Django handles authentication and how you would add a custom user model."
        ]

    if "flask" in t:
        return [
            "Explain how routing works in Flask and how to handle GET vs POST requests.",
            "How would you structure a medium-sized Flask application (folders/modules)?",
            "How do you handle sessions in Flask securely?"
        ]

    if "react" in t:
        return [
            "Explain the difference between props and state in React.",
            "What are hooks? Give an example of useEffect and a typical use case.",
            "How does React's virtual DOM improve performance?"
        ]

    if "sql" in t or "mysql" in t or "postgres" in t or "postgresql" in t:
        return [
            "Explain the difference between INNER JOIN and LEFT JOIN with an example.",
            "How do you create an index and when should you use it?",
            "Write an SQL query to find duplicate rows based on a combination of columns."
        ]

    if "aws" in t or "gcp" in t or "azure" in t:
        return [
            "Explain how you would design a scalable web app on the cloud (basic components).",
            "What is the purpose of load balancers and auto-scaling groups?",
            "How do you securely store and retrieve secrets/configuration in cloud deployments?"
        ]

    if "java" in t:
        return [
            "Explain the difference between JDK, JRE, and JVM.",
            "What is the difference between equals() and == in Java?",
            "Describe how garbage collection works in Java and how you can tune it."
        ]

    if "javascript" in t or "js" == t:
        return [
            "Explain event loop and call stack in JavaScript.",
            "What is the difference between var, let and const?",
            "Explain closures and give a practical use case."
        ]

    # Generic fallback for unknown techs
    return [
        f"Describe your experience and key concepts of {tech}.",
        f"Give an example of a common problem you face with {tech} and how you solved it.",
        f"Write or describe a small code snippet or workflow demonstrating proficiency with {tech}."
    ]
