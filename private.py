class Demo:
    
    def __init__(self):
       self.name ="Public member"
       self.__age = 21
       self.__salary = 5000
    
    def show(self):
         print("Inside the class : ")
         print("public :", self.name)
         print("protected : ",self.__salary)
         print("private : ",self.__age)

obj =Demo()
obj.show()         