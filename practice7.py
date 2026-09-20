def digit_count(x):
  count = 0
  while x>0:
    digit = x%10
    count +=1
    x =x//10
  
    print (digit)
  return count
value = int(input("enter a number: "))
print ("Number of digits: ", digit_count(value))



