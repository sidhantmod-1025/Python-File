import os
import random
from dotenv import load_dotenv
from groq import Groq

# 1. API Key ko sahi se environment variable se nikalen (Ya direct string daal dein agar test kar rahe hain)
# Apne system/env me key ka naam sahi se check kar lena (e.g., "GROQ_API_KEY")
load_dotenv()
api_key = os.getenv("GROQ_API_KEY") 

client = Groq(api_key=api_key)

# Global variables ke bina manage karne ke liye dictionary best hai
chat_state = {"name": ""}

def chatbot(user_input):
    # original casing capture karne ke liye lower() sirf matching k liye use karenge
    user_clean = user_input.strip().lower()
    
    # 2. Name check karne ka logic
    if user_clean.startswith("my name is"):
        # Original input se name nikalenge taaki name ka Pehla letter Capital rahe
        name = user_input[10:].strip() 
        chat_state["name"] = name
        return f"Nice to meet you, {name}!"
        
    elif user_clean == "what is my name":
        if chat_state["name"]:
            return f"Your name is {chat_state['name']}."
        else:
            return "You haven't told me your name yet."
            
    elif user_clean in ["hello", "hi"]:
        if chat_state["name"]:
            return random.choice([
                f"Hello {chat_state['name']}!", 
                f"Hi {chat_state['name']}! Kaise ho?", 
                f"Hey {chat_state['name']}! Kya haal hai?"
            ])
        else:
            return random.choice([
                "Hello!", 
                "Hi, kaise ho?", 
                "Hey! Kya haal hai?"
            ])
            
    elif user_clean == "how are you":
        return random.choice([
            "Main bilkul thik hu!", 
            "Main badhiya hoon.", 
            "I am good! Thanks."
        ])
        
    elif user_clean == "what is your name":
        return "My name is Python chat bot!"
        
    elif user_clean == "who are you":
        return "Mai ek simple chatbot hoon!"
        
    else:
        # 3. Groq API Call
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful chatbot. Answer in simple Hinglish."
                    },
                    {
                        "role": "user",
                        "content": user_input # Original input bhejenge Groq ko
                    }
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Oops! Groq API me error aaya: {e}"

# --- Main Loop ---
print("Bot: Hello! Mai online hu. (Type 'bye' to exit)")
while True:
    user = input("You : ") # loop ke andar lowercase mat karo abhi
    if user.strip().lower() == "bye":
        print("Bot : Bye! Phir milte hai.")
        break
        
    response = chatbot(user)
    print("Bot:", response)