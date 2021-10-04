# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:35:00 2021

@author: joaqu
"""
import heapq 
class Heap(object):
    def __init__(self):
        self.item = []
        
    def parent(self, i):
        if i == 0:
            return
        return (i-1) // 2
    
    def display(self):
        print(self.item)
    
    def insert(self, new_item):
        self.item.append(new_item)
        index = len(self.item) - 1
        while index > 0 and new_item < self.item[ self.parent(index) ]:
            self.item[index] = self.item[self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = new_item
    
    
if __name__ == "__main__":
    print('start\n')
    
    h1 = [20, 14, 18, 7, 3, 1, 40, 56]
    h2 = []
    
    for i in h1:
        heapq.heappush(h2, i)
    
    print(h2)
    # heapq.heappop()
    # heapq.heappushpop(h2, 77)
    # heapq.heapreplace(h2, 5)
    # heapq.nlargest(3, h2)