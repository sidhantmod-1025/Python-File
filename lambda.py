# Square Find
square=lambda x : x*x
print(square(5))

# Add Two Variable
Add = lambda a,b : a+b
print(Add(10,20))

# Find Cube
Cube = lambda  y : y**3
print(Cube(3))

# Find Multiply
multipy = lambda c,d : c*d
print(multipy(3,2))

# Find Half
Half = lambda e : e/2
print(Half(10))

 # Find Even or Odd
value = int(input("Enter a number : "))
EvenOrodd = lambda value: "Even" if value%2==0 else "Odd"
print(EvenOrodd(value))

# Find grate value
value1 = int(input("Enter a number one : "))
value2 = int(input("Enter a number second : "))
greate = lambda value1, value2:"Greate value 1" if value1>value2 else "greater value 2"
print(greate(value1,value2))

# Find Minimum number 
value3 = int(input("Enter a number 3: "))
value4 = int(input("Enter a number 4: "))
Minimum = lambda value3, value4:"minimum value 3" if value3<value4 else "Minimum value 4"
print(Minimum(value3,value4))


# Check number is Positive Negative or Zero 
value5 =int(input("Enter number 5"))
check = lambda value5 : "positive" if value5>0 else ("Negative" if value5<0 else "Zero")
print(check(value5))


#Find three to max
max2 = lambda g,h,i : "Max a" if g>h and g>i else("max h" if h>g and h>i else "max i" )
print("Maximum value is " ,max(12,45,69))