# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:32:34 2021

@author: joaquin
"""


class Node(object):
    
    #Constructor takes in 2 optional parameters 'data' and 'next'. default parameters are 'None'
    def __init__(self, data = None, next = None):
        self.data = data # 'data' attribute holds integers
        self.next = next # 'next' attribute holds the pointer to next node
        
    #Method takes in a node as a parameter and returns the next node
    def get_next(self):
        return self.next
    
    #Method takes in a node as a parameter and returns the data
    def get_data(self):
        return self.data
    
    #Method takes in a node and integer to update the 'data' and returns nothing
    def set_data(self, newItem):
        self.data = newItem
        
    #Method takes in 2 nodes one for self and another to set the next node and returns nothing
    def set_next(self, nextNode):
        self.next = nextNode
        