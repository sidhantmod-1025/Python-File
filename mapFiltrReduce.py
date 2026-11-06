#list ke har number ka Square
number = [1,2,3,4,5]
result = map(lambda x : x*x,number)
print("Square all number",list(result))

#Har number ka double karo
Number = [1,2,3,4,5]
result=map(lambda x:x+x,Number)
print("Double All Number",list(result))

# Use Filter () function to find Even Number.
numbers=[12,10,23,34,56]
result=filter(lambda x : x%2==0 ,numbers)
print("Only Even NUmber",list(result))

# Find The greater !0 
number=[12,23,45,3,34,5,2,4,3,67,45,7]
result = filter(lambda x : x>10 ,number)
print("Greate Than 10",list(result))

# Use Reduce() Function to find The Sum 
from functools import reduce
number=[1,2,3,4,5]
result=reduce(lambda x,y: x+y,number)
print("Reduce All Number",(result))

# Use Reduce function to find Multiplication 
from functools import reduce
number=[1,2,3,4,5]
result=reduce(lambda x,y: x*y,number)
print("Reduce All Number",(result))


# MEDIUM LEVEL QUESTIONS 

#Use map to find Cube

number =[2,3,4,5]
reslt =map(lambda x : x**3 ,number)
print("Cube All Number",list(reslt))

# Use Filter To Find Only Negative Number 
numbers = [-5, 10, -2, 8, -9, 0]
result =filter(lambda x : x<0, numbers)
print("Only Negative Number",list(result))

# Use reduce to find  Maximum Number 
from functools import reduce
numbers = [12, 45, 23, 67, 34]
result = reduce(lambda x,y: x if x>y else y ,numbers)
print("Multiple by reduce",result)


#Use map function to convert uppercase
names = ["sid", "rahul", "aman"]
result =map(lambda x:x.upper() ,names)
print("Convert in upperCase",list(result))

# Use filter function to find Age Eligibility
#18 ya usse zyada age wale persons select karo.

ages = [12, 18, 21, 15, 25, 16]
result = filter(lambda x: x>=18, ages)
print("The Eligiblity ",list(result))

#. map() + filter()

#Pehle even numbers filter karo, phir unka square find karo.

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x : x%2==0,numbers)
store =result
print("Only Even Number",list(store))
result2 = map(lambda y:y*2,numbers)
print("jo even the uska square",list(result2))

# ===================HARD QUESTIONS================

# har number ke sath Even or Odd print ho
numbers = [1, 2, 3, 4, 5]
reslut = map(lambda x: "even" if x%2==0 else "odd",numbers)
print("Even or Odd",list(reslut))