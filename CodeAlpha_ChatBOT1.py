def welcome():
    print("Emomo: Hi, I'm Emomo 💙")
    print("Emomo: I'm here if you need someone to talk to.")

def get_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input:
        return "Hello. How are you feeling today?"
    elif "not okay" in user_input or "not ok" in user_input:
        return "It's okay to feel that way. Want to talk about it?"
    elif "i'm okay" in user_input or "im okay" in user_input:
        return "I'm glad to hear that. Remember to take breaks too."
    elif "tired" in user_input:
        return "You’ve been strong. Rest is important. Try to relax a bit."
    elif "anxious" in user_input or "anxiety" in user_input:
        return "Take a deep breath. You're safe here. I'm with you."
    elif "happy" in user_input:
        return "That’s lovely! Cherish this moment 🌼"
    elif "alone" in user_input:
        return "You’re not alone. I'm here, and there are people who care."
    elif "bye" in user_input:
        return "Take care of yourself. I'm always here when you need me."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You don’t have to thank me. You matter 💙"
    else:
        return "I'm listening... tell me more if you’d like."

def chat():
    welcome()
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Emomo:", response)
        if "bye" in user_input.lower():
            break

# Start the mental health chatbot
chat()
