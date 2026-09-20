#Write a program to check whether a given number is a Trimorphic number or not ?
 # A number is called a Trimorphic number if its cube ends with the number itself.

def trimorphic(n):
  orignal = n
  cube = n**3
  digits = len(str(n))
  power = 10**digits

  last = cube%power
  if last == orignal:
    print("It is trimorphic number")

  else:
    print("It is not a trimorphic number")  


value = int(input("Enter a number : "))
trimorphic(value)

"""
def trimorphic (n):
   cube = n**3
   if str(cube).endswith(str(n)):
     print("trimporphic")
   else:
     print("not tramorphic")

value = int(input("Enter a number : ))   
trimorphic(value)  
"""
