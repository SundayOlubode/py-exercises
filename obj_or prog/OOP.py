# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:12:22 2021

@author: user
"""

class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)
    
an = PartyAnimal()
an.party()
an.party()
#an = 30
#print(an)
an.party()

#PartyAnimal.party(an)
mike = list()
mike.append('wale')
mike.append('bola')
mike.append('wumi')
list.sort(mike)
print(mike)


class sam:
    n = 0
    name = 'gb'
    
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'created!')
    def mike(self):
        print(self.name, 'has a count', self.n +1)

bola = sam('wale')
bola.mike()
print(bola)
        