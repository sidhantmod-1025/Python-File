# Amstrong number
#def is_armstrong(n):
    #sum =0
    #temp =n
    #count =0
   # while n>0:
        #digit = n%10
        #count += 1
        #power = digit
        #power = len(str(temp))
        #sum = sum + digit**power
        #n = n//10
     
    #return sum

#value = int(input("Enter a number: "))
##print(is_armstrong(value))


def is_armstrong(n):
  sum = 0
  tem = n
  count = 0
  while n>0:
     digit =n%10
     count +=1
     power =digit
     power =len(str(tem))
     sum = sum + digit**power
     n = n//10

  return sum 
  
value = int (input("Enter a number: "))
print(is_armstrong(value))
