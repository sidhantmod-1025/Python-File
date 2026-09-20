# how to find sum of digits of a number? product of digit and also find strong number
from itertools import product


def sum_of_digits(x):
  sum=0
  product =1
  while x>0:
    digit =x%10
    sum =sum + digit
    product =product *digit
    x=x//10
    
  return sum, product

value = int(input("enter a number: "))
sum_result, product_result = sum_of_digits(value)
print("Sum of digits: ", sum_result)
print("Product of digits: ", product_result)

if(sum_result == product_result):
  print("The sum and product of digits are equal. so it is  a strong number")
else:
  print("The sum and product of digits are not equal. so it is not a strong number")