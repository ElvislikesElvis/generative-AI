# simple_ai.py
responses = {
    "hi": "Hello!",
    "how are you": "I'm fine!",
    "what's your name": "I'm a simple Python AI",
    "bye": "Goodbye!"
}


while True:
    user = input("You: ").lower()
    if user == "exit":
        break
    print("AI:", responses.get(user, "I don't understand."))

