# GUSSING GAME 
import random 
def guess(n):
  num = random.randint(1,100)
  print(num)
  
  if n<=1 or n<=10:
    print("Number is too low!")
  elif(n<=30 or n>=80):
    print("Number is low high")
   
  elif(n>=91 or n<=100):
    print("Number is two high")  

  elif(n==num):
    print ("you guess the correct number ")  

value = int(input("Enter a number :- "))  
guess(value)