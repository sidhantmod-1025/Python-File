# Automosphic no => Take a number as input and check whether it is an automorphic number or not. An automorphic number is a number whose square ends with the same digits as the number itself.

def squar(x): 
  sqr = x**2 
  while x>0:
    digit = len(str(x))
    lastdigit = sqr%(10**digit)
    if x == lastdigit:
      return "yes it is a   Automosphic"
    else:
      return "no it is not   Automosphic"
 
num = int(input("Enter a number :"))  
print(squar(num))