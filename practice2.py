m=int(input("Print enter the number of m "))
n=int(input("Print enter the number of n "))
print("The power of  m is", m**n )

#loop se
ans =1
for i in range (1,n+1,1):
    ans = ans*m

print("The result in loop is ", ans)    