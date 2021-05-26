# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:43:21 2021

@author: joaquin
"""

class Node(object):
    def _init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data
    
    def set_data(self, newItem):
        self.data = newItem
        