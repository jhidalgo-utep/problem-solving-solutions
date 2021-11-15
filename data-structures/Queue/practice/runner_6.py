# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:42:03 2021

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
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        
        while iter_node:
            print(iter_node, end= ' ')
            iter_node = iter_node.get_next()
            
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
        
        old_head = self.head
        self.head = self.head.get_next()
        
        return old_head.get_next()
    
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()
    
    
            
    
    
    
    
    
    