import math

def is_prime(n):
    limit = math.isqrt(n)
    if n <= 0:
        return False

    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True


value = int(input("Enter the value of n: "))

count = 0
num = value + 1

while count < 5:
    if is_prime(num):
        print(num)
        count += 1
    num += 1