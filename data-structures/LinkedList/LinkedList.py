# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:34:02 2021

@author: joaquin
"""

from Node import Node

class LinkedList(object):
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    
    def isEmpty2(self):
        return self.head == None
    
    def insert2(self, newItem):
        if LinkedList.isEmpty2(self):
            self.head = Node(newItem)
            self.tail = self.head
        else:
            Node.set_next(self.tail, Node(newItem))
            # self.tail.next = Node(newItem)
            # self.tail = self.tail.next
            self.tail = Node.get_next(self.tail)
            
            
        
    def printLL2(self):
        if LinkedList.isEmpty2(self):
            print("EMPTY LINKED LIST")
            return
        iter = self.head
        while iter != None:
            print(iter.data)
            iter = Node.get_next(iter)