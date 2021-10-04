# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:25:02 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item 
        self.next = next
        
    def get_next(self):
        return self.next
    
    def get_item(self):
        return self.item
    

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
    
    
    def pop(self):
        if self.is_empty():
            return
        val = self.head.get_item()
        self.head = self.head.get_next()
        return val
    
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end=' ')
            iter_node = iter_node.get_next()
        print('')
        
    
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
    
    
    
if __name__ == "__main__":
    print('start\n')
    q = Queue()
    q.insert(44)
    q.insert(44)
    q.insert(90)
    q.insert(3)
    q.insert(42)
    q.insert(50)
    
    q.display()
    q.pop()
    
    q.display()
    q.insert(28)
    
    q.display()
    q.pop()
    
    q.display()
    q.insert(74)
    
    q.display()
    
    q1 = []
    n = [2,4,6,7,9,11]
    for i in n:
        q1.append(i)
        
    # q1.pop(0)
        
    for i in range(len(q1) ):
        print(q1[i])