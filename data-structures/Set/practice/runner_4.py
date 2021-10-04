# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:08:02 2021

@author: joaqu
"""

class Set(object):
    def __init__(self):
        self.item = []
    
    def insert(self, new_item):
        for i in range(len(self.item) ):
            if new_item == self.item[i]:
                return
        self.item.append(new_item)
    
    
    def display(self):
        print(self.item )
        
    def remove(self, key):
        # self.item.remove(key)
        index = -1
        for i in range(len(self.item) ):
            if self.item[i] == key:
                index = i
                break
        self.item.pop(index)
    
    
            
            
        
        

if __name__ == "__main__":
    print('start\n')
    
    s = Set()
    s.insert(75)
    s.insert(30)
    s.insert(90)
    s.insert(13)
    s.insert(30)
    s.remove(30)
    s.insert(90)
    s.display()
    
    print('\n')
    s1 = set()
    s1.add(23)
    s1.add(23)
    s1.add(90)
    s1.add(54)
    print(s1)
    s1.remove(54)
    print(s1)
    
    s3=s1.union(s2)
    
    