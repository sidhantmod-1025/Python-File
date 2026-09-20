#User will entered two number . you have to print wwhether they are co-prime or not
def coprime(n ,m):
 count = 1
 for i in range (1 ,min(n,m)+1):
   if n%i==0 and m%i==0:
    count +=1
 if count ==1:
  print("it is co-prime number ")

 else:  
  print("it is not a co-prime number ")

n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
coprime(n,m)