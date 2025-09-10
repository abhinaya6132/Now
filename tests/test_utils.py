from app.utils import generate_questions

def test_generate_questions():
    qs = generate_questions(["Python", "Django"])
    assert len(qs) >= 2
