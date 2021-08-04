# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:13:50 2021

@author: joaqu
"""
from Node import Node

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_items = 0
    
    def insert(self, new_item):
        if self.head == None:
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
    
    def pop(self):
        if self.head == None:
            return None
        pop_node = self.head
        self.head = self.head.next
        return pop_node.get_item()
    
    def display(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
    
    def peak(self):
        if self.head == None:
            return
        return self.head.get_item()
            
            