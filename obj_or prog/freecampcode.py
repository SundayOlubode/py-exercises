# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:25:57 2021

@author: user
"""

class item:
    #defining class attribute
    pay_rate = 0.8
    all = list()
    def __init__(self, name: str, price: int, quantity = 3):
        #Validation
        assert price >= 0, f'Price {price} is not less than zero'
        assert quantity >= 0, f'Quantity {quantity} is not less than zero'
        
        #defining instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #action to execute
        item.all.append(self)
        
    def calc_bill(self):
        return (self.price * self.quantity)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate #can not be modified if 'item.pay_rate' is used
        return self.price

item1 = item('Laptop', 2)

#print(item.__dict__) #All attributes at class level (in dict) 
#print(item1.__dict__) ##All attributes at instance level (in dict)

#print(item1.price)
#print(item1.pay_rate)


item2 = item('iphone', 650)
item2.pay_rate = 0.7
print(item2.apply_discount())

item3 = item('samsung', 800)
item4 = item('airod', 900)
item5 = item('watch', 950)
item6 = item('tablet', 700)

for instance in item.all:
    print(instance.name)