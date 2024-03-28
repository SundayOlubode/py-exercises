# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:34:54 2021

@author: user
"""

class Person:
    def getName(self):
        print('Harry')
    def getAge(self):
        print(13)
p = Person()
p.getName()

#wwith __init__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print('Your name is ', self.name)
    def getAge(self):
        print('Your age is ', self.age)
p1 = Person('Rhoda', 20)
p1.getName()
p1.getAge()

class college:
    def lautech(self):
        print('lautech is a tech college')
    def ui(self):
        print('UI is a science-based college')
c = college()
c.lautech()

class snacks:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getName(self):
        print('the snack is ', self.name)
    def getPrice(self):
        print('the price is '+ self.price)
s = snacks('Bun', '$10')
s.getName()


# INHERITANCE
class parent:
    def __init__(self):
        print('this is the parent class')
    def parentfunc(self):
        print('this is the parent func')
    def test(self):
        print('parent')
p = parent()
p.parentfunc()
class child(parent):
    def __init__(self):
        print('this is the child class')
    def childfunc(self):
        print('this is the child func')
    def test(self):
        print('child')
c = child()
c.parentfunc()
c.test() # this will override the 'test()' in parent() to print 'child' 

