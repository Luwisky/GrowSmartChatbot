# growchat.py

print("Welcome to GrowSmart Teachable Chatbot!")
print("Type 'exit' to quit.\n")

# Predefined Q&A
qa_pairs = {
    "hello": "Hi there! How can I help you today?",
    "what is python": "Python is a high-level, versatile programming language."
}

while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Ending chat. Goodbye!")
        break

    # Flexible keyword matching
    matched = False
    for key in qa_pairs:
        if key in user_input:
            print("Bot:", qa_pairs[key], "\n")
            matched = True
            break

    if not matched:
        print("Bot: I don't know that yet. Can you teach me?")
        new_answer = input("Your answer: ")
        qa_pairs[user_input] = new_answer
        print("Bot: Got it! I learned something new.\n")
