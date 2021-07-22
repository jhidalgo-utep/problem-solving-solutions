# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:38 2021

@author: joaqu
"""

class Heap(object):
    def __init__(self):
        self.item = []
        self.num_of_items = 0
    
    
    def parent(self, index):
        return (index-1) // 2
    
    
    def left_child(self, index):
        return (2 * index) + 1
    
    
    def right_child(self, index):
        return (2 * index) + 2
    
    
    def get_sibbling(self, index):
        if index == 0:
            return -1
        #even
        if index % 2 == 0:
            return self.item[index - 1]
        else:
            #checks if index is the last node in heap, if so, it doesnt have a sibbling
            if self.num_of_items - 1 == index:
                return -1
            return self.item[index + 1]
        
        
    def insert(self, new_item):
        
        self.item.append(new_item)
        index = len(self.item) - 1
        
        #---SETS TO A MAX HEAP HERE ---
        while index > 0 and new_item > self.item[ self.parent(index) ]:
            self.item[index] = self.item[ self.parent(index) ]
            index = self.parent(index)
        self.item[index] = new_item
        
        #increase num of items in heap
        self.num_of_items += 1
        
    
    def insert_list_to_heap(self, list_of_items):
        for item in list_of_items:
            self.insert(item)
    
    
    def display(self):
        for item in self.item:
            print(item, end = ' ')
        print()
            
    
    
if __name__ == "__main__":
    print('start program\n')
    
    ages = [56, 24, 90, 3, 200]
    
    
    h = Heap()
    h.insert_list_to_heap(ages)
    h.display()
    
    

    