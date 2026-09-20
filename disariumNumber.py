# A number is called a Disarium Number if the sum of its digits raised to the power of their respective position is equal to original number. 
# The position of digits starts from 1, counting from the left.

def disarium(n):
  original =n
  sum =0
  digits = len(str(n))
  for i in range(digits):
    digit = n%10
    sum =sum + digit**(digits-i)
    n =n//10

  if sum == original:
    print("Disarium Number")
  else:
    print("Not Disarium Number")    


value = int(input("Enter a digit :"))
disarium(value)  