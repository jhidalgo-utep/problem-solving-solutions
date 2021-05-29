# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:34:02 2021

@author: joaquin
"""

from Node import Node


class LinkedList(object):
    
    #Constructor takes in 2 optional parameters that set to 'None' as default
    def __init__(self, head = None, tail = None):
        self.head = head # 'head' attribute holds the start of the list
        self.tail = tail # 'tail' attribute holds the end of the list
        
    #Method takes in a LinkedList and returns a boolean checking if LinkedList is empty
    def isEmpty(self):
        return self.head == None
    
    #Method takes in a LinkedList and integer but returns nothing. Method inserts new node to end of list
    def insert(self, newItem):
        if LinkedList.isEmpty(self):
            self.head = Node(newItem)
            self.tail = self.head
        else:
            Node.set_next(self.tail, Node(newItem)) #makes tail of linkedlist point to the new node created
            self.tail = Node.get_next(self.tail) #updates tail node to the new node created
        
    #Method takes in a LinkedList and returns nothing. Method prints all 'node.data' of each node
    def printList(self):
        if LinkedList.isEmpty(self):
            print("EMPTY LINKED LIST")
            return
        iter = self.head
        while iter != None:
            print(iter.data)
            iter = Node.get_next(iter)
            
    def get_head_data(self):
        return self.head.data
    
    def get_tail_data(self):
        return self.tail.data
    
    def get_head_node(self):
        return self.head
    
    def get_tail_node(self):
        return self.tail