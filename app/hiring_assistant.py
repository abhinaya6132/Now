import streamlit as st
from datetime import datetime

# Helper function to generate sample technical questions
def generate_questions(tech_stack):
    questions = []
    
    if 'Python' in tech_stack:
        questions.extend([
            "What is a Python decorator and how do you use it?",
            "Explain the difference between a list and a tuple in Python.",
            "What are Python generators?",
            "Explain Python's GIL (Global Interpreter Lock).",
            "What is the difference between deep copy and shallow copy in Python?",
            "How does Python handle memory management?"
        ])
        
    if 'Django' in tech_stack:
        questions.extend([
            "How do you create a model in Django?",
            "What is the role of middleware in Django?",
            "Explain Django ORM and how it works.",
            "How do you handle forms in Django?",
            "What is the difference between Django templates and Jinja templates?"
        ])
        
    if 'JavaScript' in tech_stack:
        questions.extend([
            "What is the difference between var, let, and const?",
            "Explain event delegation in JavaScript.",
            "What are closures in JavaScript?",
            "Explain the difference between == and === in JS.",
            "What is the purpose of the 'this' keyword?"
        ])
        
    if 'React' in tech_stack:
        questions.extend([
            "What is JSX?",
            "Explain the virtual DOM in React.",
            "What are React hooks and why are they useful?",
            "What is the difference between state and props in React?",
            "How does React handle component lifecycle?"
        ])
        
    if 'Node.js' in tech_stack:
        questions.extend([
            "What is the event loop in Node.js?",
            "Explain the difference between synchronous and asynchronous programming in Node.js.",
            "How do you handle errors in Node.js?",
            "What are streams in Node.js?",
            "What is the difference between require and import in Node.js?"
        ])
        
    if 'SQL' in tech_stack:
        questions.extend([
            "What is a JOIN in SQL?",
            "Explain the difference between primary key and foreign key.",
            "What is normalization in databases?",
            "What is the difference between INNER JOIN and OUTER JOIN?",
            "How do you optimize SQL queries for performance?"
        ])
        
    if 'NoSQL' in tech_stack:
        questions.extend([
            "What is a document database?",
            "Difference between SQL and NoSQL databases?",
            "Explain how MongoDB stores data.",
            "What is denormalization in NoSQL databases?",
            "Explain eventual consistency in NoSQL systems."
        ])
    
    return questions

# Streamlit UI
st.title("🧑‍💼 Hiring Assistant Chatbot")
st.write("Welcome! Please fill in the following details:")

# Candidate Details
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
position = st.text_input("Desired Position(s)")
location = st.text_input("Current Location")
tech_stack = st.multiselect(
    "Select your Tech Stack",
    ['Python', 'Django', 'JavaScript', 'React', 'Node.js', 'SQL', 'NoSQL']
)

if st.button("Generate Technical Questions"):
    if not full_name or not email or not tech_stack:
        st.warning("Please fill in all required fields and select at least one tech stack.")
    else:
        st.success(f"Thank you {full_name}! Here are your technical questions:")

        # Get all questions for the selected tech stacks
        questions = generate_questions(tech_stack)
        
        # Show the first 5 questions consistently
        questions_to_show = questions[:5]
        
        for i, q in enumerate(questions_to_show, 1):
            st.write(f"{i}. {q}")

        st.write("End of questions. Thank you for your time!")
        st.write(f"Session Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
