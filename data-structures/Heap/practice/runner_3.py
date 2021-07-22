# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 19:24:46 2021

@author: joaqu
"""

class Heap(object):
    def __init__(self):
        self.item = []
        self.num_of_items = 0
    
    def parent(self, index):
        return (index-1) // 2
    
    def left_child(self, index):
        return (index*2) + 1
    
    def right_child(self, index):
        return (index*2) + 2
    
    def sibbling(self, index):
        if index <= 0:
            return -1
        
        if index > self.num_of_items-1:
            return -1
        
        if index %2 == 0:
            return self.item[ index - 1 ]
        else:
            if index >= self.num_of_items - 1:
                return -1
            return self.item[ index + 1 ]
                
    
    def insert(self, new_item):
        self.item.append(new_item)
        
        index = len(self.item) - 1
        
        #keeps moving down the parent node until new_item finds its perfect spot in its subtree
        while index > 0 and new_item > self.item[ self.parent(index) ]:
            self.item[index] = self.item[self.parent(index)]
            index = self.parent(index)
            
        self.item[index] = new_item
        
        self.num_of_items += 1
        
    
    def display(self):
        if len(self.item) == 0:
            return
        for item in self.item:
            print(item, end= ' ')
        print()
        
        
    def insert_list_to_heap(self, my_list):
        for item in my_list:
            self.insert(item)
        
        

if __name__ == "__main__":
    print('start program\n')
    
    ages = [34, 37, 26, 10, 3, 90]
    h = Heap()
    h.insert_list_to_heap(ages)
    h.display()
    
    
    