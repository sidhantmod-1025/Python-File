# i will give you two number .you will tell whether they are consecutive fibonacci or not 

def consecutive(n):
  first = 0
  second =1
  next =0

  
  num1 = int(input("Enter a first number"))
  num2 = int(input("Enter a second number"))



  print(first)
  print (second)
  for i in range (2, n+1):
    if first ==num1 and second==num2:
         print("it is aconsecutive")
         return 

    next = first + second
    first = second
    second = next
    result = next
    print(next)
  else:
     print("it is not a consuctive")
a = int(input("Enter a number : "))
print(consecutive(a))