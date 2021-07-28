# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:44:57 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, new_item = None, next = None):
        self.item = new_item
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, new_item):
        if self.head == None:
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.next
    
    def pop(self):
        if self.head == None:
            return
        self.head = self.head.next
        
    
    def display(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.item)
            iter_node = iter_node.next
        print('\n')
        
    def peak(self):
        if self.head == None:
            return
        return self.head.item
        
        

if __name__ == "__main__":
    print('start program\n')
    
    q = Queue()
    q.insert(21)
    q.insert(49)
    q.insert(57)
    q.insert(74)
    q.display()
    q.pop()
    q.display()
    print(q.peak())