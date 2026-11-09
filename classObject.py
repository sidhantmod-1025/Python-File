#First Practice
class Student:
  name = "sidhant"
  age= 21
s1 =Student()
print(s1.name)
print(s1.age)

#Create Car 
class Car:
  brand="BMW"
  color="Black"

c1 =Car()

print("Car Brand :- ",c1.brand)
print("Car Color :- ",c1.color)

# Create Mobile 

class mobile:
  brand="Moto G85"
  price="18,000"
  color="Green"
  battery="5,000"
  sms="jio"
  performance="Good"
  storage ="8 gb RAM,128Gb ROM"
  Camera ="5HV" 

m1=mobile()  
m2=mobile()  
m3=mobile()  
m4=mobile()  
m5=mobile()  
m6=mobile()  
m7=mobile()  
m8=mobile()  
print("Brand",m1.brand)
print("Price",m2.price)
print("Color",m3.color)
print("Battery",m4.battery)
print("sms",m5.sms)
print("Performance",m6.performance)
print("Storage",m7.storage)
print("Camera",m8.Camera) 


# Object  Attribute 

class Student:
  name ="Sidjant"

s1= Student()
s2= Student()

s1.age=21
s2.age=32


print(s1.name,s1.age)
print(s2.name,s2.age)


# Mobile Class Create Kro 
class Mobile:
  def __init__(self,brand,price,color):
    self.brand = brand
    self.price =price
    self.color=color

  def display(self):
    print("Brand",self.brand)
    print("Price",self.price)
    print("Color",self.color)

m1 = Mobile("Apple",10000,"Green")   
m2 = Mobile("Oppo",20000,"yellow") 
m3 = Mobile("Samsung",30000,"purple")   

m1.display()
m2.display()
m3.display()

# Employee Name 
class Employee:
  def __init__(self,name,id,salary):
    self.name=name
    self.id=id
    self.salary=salary

  def display(self):
    print("Name : ",self.name)
    print("ID : ",self.id)
    print("Salary : ",self.salary)

m1 = Employee("Sidhant ",22,1000000)
m2 = Employee("Rahul ",34,102903)
m3= Employee("Sahil",12,23903)

m1.display()
m2.display()
m3.display()

# Rectangle Class 
class Rectangle:
  def __init__(self,length,breadth):
    self.Area = length * breadth
    

  def display(self):
    print("Area of rectangle is   : ",self.Area)  

m1 = Rectangle(2 ,3)

m1.display()

# Multiple Student class 

class Student:
  def __init__(self,name,rollNumber ,marks):
    self.name=name
    self.rollnumber=rollNumber
    self.marks=marks

  def display(self):
    print("Name : ",self.name)
    print("rollNumber : ",self.rollnumber)
    print("Marks : ",self.marks)

m1 = Student("Sidhant ",22,95)
m2 = Student("Rahul ",34,65)
m3= Student("Sahil",12,89)

m1.display()
m2.display()
m3.display()


