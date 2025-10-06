class Car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return (self.make)
    
    def get_info(self):
        return (f'{self.model} {self.year}')


my_car = Car('Toyota', 'Corolla', '2020')
print (my_car.get_make())
print(f'{my_car.get_make()} , {my_car.get_info()}')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)
    
    def perimiter(self):
        return(self.width + self.height)

rectangle = Rectangle(5, 10)
print(rectangle.area())
print(rectangle.perimiter())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def getInfo(self):
        return (f'{self.owner}')

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

myAccount = BankAccount('John')

newBalance = myAccount.deposit(100)
afterWithdraw = myAccount.withdraw(50)

print(myAccount.owner)
print(newBalance)
print(afterWithdraw)


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avarage(self):
        return sum(self.grades) / len(self.grades)
        
    def addGrade(self, grade):
        self.grades.append(grade)
        return self.grades
        


student = Student('John', [80,90,100])

print (student.addGrade(95))
print(student.avarage())


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self, times):
        return ("Woof! " * times)
    
    def birthday(self):
        self.age += 1
        return (f'Happy birthday {myDog.name}! You are now {self.age} years old.')


myDog = Dog('Bob', 3)

print(f'{myDog.bark(3)}({myDog.name})')
print(f'{myDog.birthday()}')


