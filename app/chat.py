from context_manager import ContextManager

def generate_response(user_input, context_manager):
    context_manager.add_message(user_input)

    # Simple fallback response
    return "Thank you for your input! The next steps will be communicated soon."
