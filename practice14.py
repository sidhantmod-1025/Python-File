#Calculate Fibonacci series

def fibo(n):
    first_value =0
    second_value =1
    print("First value",first_value)
    print("Second value",second_value)
    print(first_value + second_value)
    for i in range (2 , n+1  ):
        next_value= first_value + second_value
        print(next_value)
        first_value = second_value
        second_value= next_value

value = int(input("Enter a number :"))
print(fibo(value))  
  