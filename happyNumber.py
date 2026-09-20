# Write a program to check whether number is a happy number or not
# A number is calleda jappy number if you repeated replace the number by the sum of the square of its digits, and eventually the result becomes 1.
#if the process enter a cycle and never reaches 1, tje number is not a happy number

def happy(n):
  count = 0
  while n!=1: 
    sum = 0
    count = count + 1
    while n>0:
       digit = n%10  
       print("The digit is",digit)
       square = (digit*digit)
       print( "the square is",square)
       sum = sum + square
       n=n//10
    print( "The sum is",sum)     
    n = sum
    if count > 10:
      print("not a happy number")
      return
    
  if n==1:
    print("yes it is a happy number") 

  else:
    print("not a happy number")  

 
value = int(input("Enter  a  nmber :"))
happy(value)  