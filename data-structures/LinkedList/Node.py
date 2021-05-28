# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:32:34 2021

@author: joaquin
"""

#Node Class
class Node(object):
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data
    
    def set_data(self, newItem):
        self.data = newItem
        
    def set_next(self, nextNode):
        self.next = nextNode