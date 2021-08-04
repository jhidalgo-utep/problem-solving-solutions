# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:21:34 2021

@author: joaqu
"""

class Set(object):
    def __init__(self):
        self.item = []
    
    def insert(self, new_item):
        for i in self.item:
            if i == new_item:
                return
        self.item.append(new_item)
    
    def pop(self, key_item):
        for i in self.item:
            if i == key_item:
                self.item.remove(key_item)
        
        
    def display(self):
        if self == None:
            return
        print(self.item)
        print()
                
    