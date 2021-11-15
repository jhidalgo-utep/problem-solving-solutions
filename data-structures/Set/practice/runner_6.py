# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:51:42 2021

@author: joaqu
"""

class Set(object):
    def __init__(self):
        self.item = []
    
    def display(self):
        print(self.item)
        
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item )
        
    def delete(self, key):
        index = -1
        for i in range(len(self.item) ):
            if self.item[i] == key:
                index = key
                break
        if index >= 0:
            self.item.pop(index)
            
            
            
if __name__ == "__main__":
    print('start\n')
    s = set()
    
    s.add(44)
    s.add(89)
    s.add(20)
    s.add(55)
    print(s)
    s.remove(55)
    print(s)
        
        
        
        
        
        
        
        