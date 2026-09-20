#Adam number => given number ka Square or us square ke number ka reverse or given number ka reverse same hona chiye
import math
def reverse(n):
  rev =0 
  while n>0: 
    rem = n%10;
    rev =rev*10+rem
    n = n//10
  else:
    print("Given number Square :",rev)
      
value = int(input("Enter a number : "));
limit = value**2
print("Number of Square : ", limit)
num1= reverse(limit)
num2= reverse(value) 
if num1==num2:
  print("Adman Number")

else:
  print("not adman number")  

