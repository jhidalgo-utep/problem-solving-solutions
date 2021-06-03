# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:34:02 2021

@author: joaquin
"""

from Node import Node

# Self explanation:
# When 'self' is being passed as a parameter, 'self' is the list. 
# You can use operations like: 'self.head' & 'self.tail' to get a Node from the list.
# Also by putting 'Node. ' you are able to use operations from the Node.py class like: 'Node.get_next(self.head)' 


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
        iter_node = self.head
        while iter_node != None:
            print(iter_node.data)
            iter_node = Node.get_next(iter_node)
    
    #Method takes in a list and returns an integer length of list
    def getListLength(self):
        list_length = 0
        iter_node = self.head
        while iter_node != None:
            list_length += 1
            iter_node = Node.get_next( iter_node )
        return list_length
    
    #Method takes in a LinkedList and returns the middle index of list
    def get_middle_index(self):
        if self.head == None:
            return None
        list_length = LinkedList.getListLength(self)
        if list_length <= 2:
            return 0
        else:
            if list_length % 2 == 0:
                return list_length // 2 - 1
            else:
                return list_length // 2
            
            
    #Getters
    #Method takes in a LinkedList and returns the data of the head node
    def get_head_data(self):
        return self.head.data
    
    #Method takes in a LinkedList and returns the data of the tail node
    def get_tail_data(self):
        return self.tail.data
    
    #Method takes in a LinkedList and returns the address of the head node
    def get_head_node(self):
        return self.head
    
    #Method takes in a LinkedList and returns the address of the tail node
    def get_tail_node(self):
        return self.tail
