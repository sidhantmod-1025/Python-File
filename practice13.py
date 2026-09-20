#Harshad number => given value ke digit ka sum use ke original value se divide ho jaye toh vo harshad number hota hai

def harshad(n):
  temp =n
  sum = 0
  count = 0
  while n>0:
    digit = n%10
    count +=1
    print("The digit is ",digit)
    sum = sum + digit
    print( "The sum of the value is",sum)
    n=n//10

  if temp%sum == 0:
    return "The number is harshad"
  else:
      return "The number is not harshad"
    

value = int(input("Enter a number :"))  
print(harshad(value))