# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:54:47 2021

@author: joaqu
"""
# 7 mins

class Set(object):
    def __init__(self):
        self.item = []
    
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)
        
    def pop(self, key_item):
        for i in range(len(self.item) ):
            if self.item[i] == key_item:
                self.item.pop(i)
                return
            
    def display(self):
        print(self.item)
        
if __name__ == "__main__":
    print('start\n')
    s = Set()
    s.insert(10)
    s.insert(20)
    s.insert(30)
    s.display()
    
    
    s2 = set()
    s2.add('pizza')
    s2.add('black')
    s2.add('up')
    s2.add('cheese')
    print(s2)
    s2.remove('up')
    print(s2)
    
    s3 = set()
    s3.add('rock')
    s3.add('dirt')
    s3.add('cactus')
    
    s4 = s2.union(s3)
    print(s4)
        
            