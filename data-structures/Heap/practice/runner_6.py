# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:25:40 2021

@author: joaqu
"""
import heapq

class Heap(object):
    def __init__(self):
        self.item = []
        
    # 0, 1, 2, 3, 4, 5
    def parent(self, index):
        if index == 0:
            return
        return (index - 1) // 2
    
        
    def insert(self, new_item):
        self.item.append(new_item)
        index = len(self.item) - 1
        
        while index > 0 and new_item > self.item[self.parent(index) ]:
            self.item[index] = self.item[ self.parent(index) ]
            index = self.parent(index)
        
        self.item[index] = new_item
    
    def display(self):
        print(self.item )
        
        
if __name__ == "__main__":
    print('lets gooo\n')
    
    h = []
    heapq.heappush(h, 12)
    heapq.heappush(h, 20)
    heapq.heappush(h, 80)
    heapq.heappush(h, 50)
    heapq.heappush(h, 3)
    heapq.heappush(h, 2)
    heapq.heappop(h)
    print(h)
    
    print(heapq.nlargest(2, h) )
    print(heapq.nsmallest(3, h))
    
    
    
    
    
            
        
        
        
        
        
        