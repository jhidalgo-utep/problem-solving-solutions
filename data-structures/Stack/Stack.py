# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:56:57 2021

@author: joaqu
"""
from Node import Node

class Stack(object):
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.head == None:
            self.head = Node(new_item)
        else:
            old_head = self.head
            self.head = Node(new_item, old_head)
    
    def pop(self):
        if self.head == None:
            return
        pop_item = self.head
        self.head = self.head.get_next()
        return pop_item.get_item()
    
    def display(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item() )
            iter_node = iter_node.get_next()
        print()
        
    def peak(self):
        if self.is_empty():
            return
        return self.head.get_item()