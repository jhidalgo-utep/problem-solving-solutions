# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:01:38 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    #The self parameter refers to the self class 'Node'
    def get_next_node(self):
        return self.next
    
    def get_item(self):
        return self.item

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
    
    def display(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item() )
            iter_node = iter_node.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(21)
    ll.insert(24)
    ll.insert(93)
    ll.display()