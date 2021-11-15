# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:46:13 2021

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
    

class LinkedList(object):
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
            print(iter_node.get_item() )
            iter_node = iter_node.get_next()
        print()
        
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
        
    def insert_after(self, new_item, key):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key:
                break
            iter_node = iter_node.get_next()
            
        
        
            
            
            
    
    
    
