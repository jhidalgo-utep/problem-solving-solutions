# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:46:01 2021

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

class Stack(object):
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ' )
            iter_node = iter_node.get_next()
        print()
        
    def pop(self):
        if self.is_empty():
            return None
        old_head = self.head
        self.head = self.head.get_next()
        return old_head.get_item()
    
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()


if __name__ == "__main__":
    print('start\n')
    
    s = Stack()
    s.insert(14)
    s.insert(80)
    s.insert(41)
    s.display()
    
    
    n = []
    n.append(43)
    n.append(86)
    n.append(10)
    n.pop()
    print(n)
    n.append(100)
    print(n)
    
    for i in range(len(n)-1, -1, -1):
        print( n[i])
    
    
    
    
    
            
        
        
        