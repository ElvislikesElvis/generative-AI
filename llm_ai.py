import os
import openai

# Make sure your OpenAI API key is set
# export OPENAI_API_KEY="sk-XXXX" (Linux/macOS)
# setx OPENAI_API_KEY "sk-XXXX" (Windows)

# Local fallback responses
local_responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm an AI, but I'm doing great! How about you?",
    "what is your name": "I am your simple AI assistant.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "what can you do": "I can chat with you and answer simple questions.",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!",
    "who created you": "Elvis created me.",
    "what is AI": "AI stands for Artificial Intelligence. It's about machines learning to think like humans.",
    "help": "You can say hi, ask how I am, ask for a joke, or say bye to exit."
}

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

print("AI: Hello! Type 'exit' or 'quit' to end the chat.")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye!")
        break

    # Try local response first
    response_text = local_responses.get(user_input.lower())
    
    if not response_text:
        try:
            # Call OpenAI API
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            response_text = response.choices[0].message.content.strip()
        except Exception as e:
            response_text = "I couldn't reach OpenAI. Please try again later."

    print("AI:", response_text)

