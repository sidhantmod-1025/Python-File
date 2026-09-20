#Find Pronic number => Pronic number vo number hota hai jo do consuctive  integer ko multiply krne se milta hai

def pronic (n):
  for i in range(n):
    if i * (i +1)==n:
      print("Pronic number ")
      break
  else : 
    print("Not a pronic number")  
    
n =int(input("Enter a first number : "))

pronic(n)  
