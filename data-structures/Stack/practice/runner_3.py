# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:14:45 2021

@author: joaqu
"""

# 11 mins

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next

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
    
    def pop(self):
        if self.is_empty():
            return
        popped = self.head.get_item()
        self.head = self.head.get_next()
        return popped
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end=' ')
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()

if __name__ == "__main__":
    print('start\n')
    s = Stack()
    s.insert(10)
    s.insert(20)
    s.insert(30)
    s.display()
    print(s.pop() )
    s.display()
    s.insert(500)
    s.display()
    print( s.peak() )
    
    
    s2 = []
    s2.append(0)
    s2.append(1)
    s2.append(2)
    s2.append(3)
    s2.pop()
    s2.append(4)
    s2.append(5)
    
    for i in range(len(s2)-1, -1, -1):
        print(s2[i])
    