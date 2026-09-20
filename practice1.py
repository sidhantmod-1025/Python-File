import math 

m=int(input("Print a number of m "))

x=int(math.sqrt(m))

for i in range (2,x+1):
    if(x%i ==0):
       print("It is not a prime") 
       break

else:
    print("It is a prime")      