def decorate(func):
    def wrapper ():
        print("iwill print my self before the function hello ")
        func()
        print("i Will print after the function hello")
    return wrapper
    
@decorate
def hello():
    print("hello i am akasha vays")  
    
hello()   

  
    
      