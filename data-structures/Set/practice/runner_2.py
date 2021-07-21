# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:18:02 2021

@author: joaqu
"""

class Set(object):
    def __init__(self):
        self.item = []
        self.num_of_items = 0
        
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                # self.item.remove(i)
                return
        self.item.append(new_item)
        
    def remove(self, key_item):
        for i in self.item:
            if i == key_item:
                self.item.remove(key_item)
                return
        
    def display(self):
        for i in self.item:
            print(i, end=' ')
        

if __name__ == "__main__":
    print('start program\n')
    s = Set()
    s.insert(21)
    s.insert(44)
    s.insert(19)
    s.insert(19)
    s.remove(1)
    s.display()