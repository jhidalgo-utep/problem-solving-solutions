# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:48:48 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    


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
        popped = self.head.get_item()
        self.head = self.head.get_next()
        return popped
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print( iter_node.get_item(), end = ' ' )
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
        

if __name__ == "__main__":
    print('start\n')
    q = Queue()
    q.insert(34)
    q.insert(88)
    q.insert(99)
    q.insert(37)
    q.insert(40)
    q.insert(50)
    q.display()
    print(q.pop() )
    q.display()
    print( q.peak() )
    q.insert(12)
    q.display()
    
    
    q2 = []
    q2.append(90)
    q2.append(91)
    q2.append(92)
    q2.append(93)
    q2.append(94)
    print( q2 )
    q2.remove(92)
    print( q2 )
    print( q2.index(94))
    