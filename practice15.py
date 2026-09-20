# i will give you a number you will tell me the number is a fibonacci yes or not 

def fibo (n):
  first = 0 
  second =1
  next =0
  print(first)
  print(second)
  for i in range(2, n+1):
    next = first + second 
    first =second
    second =next
    result =next
    print(result)
    if n==result:
      return "The user number is fibonanchi"
  else:
    return  " The user number is not a fibonachi"

value = int(input("Enter a number : "))
print(fibo(value))
 