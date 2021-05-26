# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:43:21 2021

@author: joaquin
"""

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
    
        
class LinkedList(object):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
def isEmpty(L):
    return L.head == None
    
def insert(L, newItem):
    if isEmpty(L):
        L.head = Node(newItem)
        L.tail = L.head
    else:
        Node.set_next(L.tail, Node(newItem))
        L.tail = L.tail.next
        
def printLL(L):
    iter = L.head
    while iter != None:
        print(iter.data)
        iter = Node.get_next(iter)

