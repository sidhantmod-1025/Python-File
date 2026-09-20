def decorate(func):
    def wrapper(a,b):
        print("The addition to your nuber are")
        func(a,b)
        print("Thankyou I hope you liked it")
    return wrapper

@decorate
def addition (a,b):
    print(f"Your total number is {a+b}")

addition(10,20)        