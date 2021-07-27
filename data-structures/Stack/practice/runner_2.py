# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:24:09 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, new_item = None, next = None):
        self.item = new_item
        self.next = next
        

class Stack(object):
    def __init__(self):
        self.head = None
        self.num_of_items = 0
        
        
    def insert(self, new_item):
        if self.head == None:
            self.head = Node(new_item)
            self.num_of_items += 1
        else:
            old_head = self.head 
            self.head = Node(new_item, old_head)
            self.num_of_items += 1

    
    def display(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.item)
            iter_node = iter_node.next
        print('\n')
    
    
    def pop(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.num_of_items -= 1


    def peak(self):
        if self.head == None:
            return
        return self.head.item

    def empty(self):
        self.head = None
        self.num_of_items = 0


if __name__ == "__main__":
    print('start program\n')
    s = Stack()
    s.insert(21)
    s.insert(37)
    s.insert(8)
    s.pop()
    s.empty()
    s.insert(99)
    s.insert(44)
    s.display()
    
    s.pop()
    s.insert(11)
    s.display()
    print( s.num_of_items)
    print(s.peak() )
    
