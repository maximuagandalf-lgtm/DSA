#Define a python class Person with instance object variables name and age.Set instance object variables in __init__method(). Also define show() method to display name and age of a Person. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print("The name is: ", self.name)
        print("The age is: ", self.age)

name = input("Enter the name of person: ")
age = int(input("Enter the age of person: "))
p1 = Person(name, age)
p1.show()

# Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.

class Circle:
    def __setattr__(self, radius):
        self.radius = radius
    
    def __getattribute__(self):
        return self.radius
    
    def getArea(self):
        area = 3.14*self.radius*self.radius
        print("Area of the circle with radius", self.radius, "is", area)
    
    def getCircumference(self):
        circumference = 2*3.14*self.radius
        print("Circumference of the circle with radius", self.radius, "is", circumference)

c1 = Circle()       #instance object
c1.__setattr__(10)
c1.__getattribute__()
c1.getArea()
c1.getCircumference()

#Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions() and getArea method in it.

class Rectangle:
    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def showDimensions(self):
        print("The length of rectangle is: ", self.length)
        print("The breadth of rectangle is: ", self.breadth)
    
    def getArea(self):
        print("Area of the rectangle is: ", self.length * self.breadth)
    
R1 = Rectangle()
R1.setDimensions(10, 20)
R1.showDimensions()
R1.getArea()

#Define a class Book with instance object variables bookid, title and price. Initialise them via __init__() method. Also define method to show book variables.

class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def show(self):
        print("The ID of book is", self.bookid, ", title is", self.title, ", price is RS.", self.price)

book1 = Book(34, "The 12 rules of life", 1200)
book1.show()

#Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.

class Team:
    def __init__(self, members = None):
        self.members = []
        n = int(input("Enter the number of members: "))
        for i in range(n):
            elem = input("Enter the name of member: ")
            self.members.append(elem)
        
    
    def show(self):
        print("The members are: ", self.members)

T1 = Team()
T1.show()