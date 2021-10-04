# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:43:23 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
    def get_node(self):
        return self.item
    
    def get_next(self):
        return self.next


class Stack(object):
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee

    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print( iter_node.get_node() )
            iter_node = iter_node.get_next()
    
    def pop(self):
        val = self.head.get_node()
        self.head = self.head.get_next()
        return val
        
    def peak(self):
        return self.head.get_node()


if __name__ == "__main__":
    print('start\n')
    s = Stack()
    s.insert(21)
    s.insert(100)
    s.insert(46)
    s.insert(87)
    s.display()
    
    print('\n')
    
    t = [4, 5, 6, 7, 8, 9]
    s2 = []
    for i in range(len(t)):
        s2.append(t[i])
        
    for i in range(len(s2)-1, -1, -1):
        print(s2[i] , end=' ')
        