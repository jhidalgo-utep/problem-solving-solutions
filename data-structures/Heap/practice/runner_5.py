# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:43:45 2021

@author: joaqu
"""
import heapq

class Heap(object):
    def __init__(self):
        self.item = []
    
    def display(self):
        print(self.item)
        
    # 0, 1, 2, 3, 4, 5
    def parent(self, index):
        if index == 0:
            return index
        return (index-1) // 2
        
    
    def insert(self, new_item):
        self.item.append(new_item)
        index = len(self.item) -1
        
        # Max Heap
        while index > 0 and new_item > self.item[self.parent(index)]:
            self.item[index] = self.item[self.parent(index) ] 
            index = self.parent(index)
        
        self.item[index] = new_item
        


if __name__ == "__main__":
    print('start\n')
    
    h = []
    heapq.heappush(h, 26)
    heapq.heappush(h, 12)
    heapq.heappush(h, 50)
    heapq.heappush(h, 4)
    heapq.heappushpop(h, 9)
    heapq.heapreplace(h, 77)
    print(h)
    
    print(heapq.nlargest(3, h))
    print(heapq.nsmallest(2, h))
    
    
    
        
        
        






