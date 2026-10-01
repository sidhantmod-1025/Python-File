import random 

name =""
def chatbot(user):
  global name
  if user.startswith("my name is"):
    name =user.replace("my name is ", "").strip()
    return f"Nice to meet you,{name}!"
  elif user =="what is my name":
     if name:
       return f"Your name is {name}."
     else:
       return" you haven't told me your name yet."

  elif user == "hello" or user=="hi":
    if name:
     return random.choice([
       f"Hello {name}!",
       f"hi{name}!kaise ho?",
       f"het{name}! kya haal hai?"
     ])
    else:
     return random.choice([
      "Hello",
      "Hi kaise ho ?",
      "Hey ! kya haal hai ?"
    ])
   

  elif user=="how are you":

   return random.choice ([
      "Main bilkul thik hu !",
      "Main badhiya hoon",
      "Iam good! Thanks"
    ])
  
  elif user == "what is your name":
   return "My name is Python chat bot !"

  elif user == "who are you":
    return "Mai ek simple chatbot hoon !"
  
  else :
    return " Sorry, mujhe ye samajh nahi aaya."
while True:
  user = input("You : ").lower().strip() 

  if user == "bye":
    print("Bot :bye! Phir milte hai ")
    break
  response=chatbot(user)

  print("Bot: ",response)