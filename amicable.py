# Write a program to chexk whether to number given are Amicable number or not 
# Two number are called Amicable number if the sum of the proper divisor of the first number is equal to the second number ,and the sum of the proper divisor  of the second number is equal to the first number.

def amicable(n,m):
  sum1 = 0
  sum2=0
  for i in range(1,n):
    if n%i==0:
      sum1 +=i
  for i in range(1,m):
    if m%i==0:
       sum2 +=i

  if sum1==m and sum2==n:
    print("Amicable number")
  else :
    print ("not Amicable number")       



n1 = int(input("Eneter a first number : "))
n2 = int(input("Eneter a second number : "))
amicable(n1,n2)
