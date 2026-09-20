# how many odd digit / even digit in a number
def odd_even_digit_count(x):
  odd_count = 0
  even_count = 0
  while x>0:
    digit = x%10
    if digit % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
    x =x//10
  return odd_count, even_count

value = int(input("enter a number: "))
odd_count, even_count = odd_even_digit_count(value)
print("Number of odd digits: ", odd_count)
print("Number of even digits: ", even_count)

  
