import math
def is_prime(n):
    limit = math.isqrt(n)
    for i in range(2,limit+1,1):
        if n%i == 0:
            return False
    else:
        return True   
    
value = int(input("Enter the value of n")) 
print(is_prime(value))