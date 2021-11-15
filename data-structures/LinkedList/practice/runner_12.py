# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:06:52 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
            
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ' )
            iter_node = iter_node.get_next()
        print()
        
    def insert_after(self, new_item, key):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key:
                break
            iter_node = iter_node.get_next()
            
        if iter_node == None:
            return
        
        next_node = iter_node.get_next()
        insertee = Node(new_item, next_node)
        iter_node.next = insertee
        if next_node == None:
            self.tail = insertee
    
    def insert_begin(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee
    
    def reverse_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        prev = None
        iter_node = old_head = self.head
        while iter_node:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
        self.head = prev
        self.tail = old_head
    
    def delete(self, key):
        if self.is_empty():
            return
        
        if self.head.get_item == key:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        prev = None
        
        while iter_node:
            if iter_node.get_item() == key:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        next_node = iter_node.get_next()
        prev.next = next_node
        
        if next_node == None:
            self.tail = prev
    
    def remove_nth(self, n):
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            
            #also i > 5 should work too
            if fast == None and i != n-1:
                return
        
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
            
        slow.next = slow.get_next().get_next()
        if slow.next == None:
            self.tail = slow
        
    
    def remove_duplicates(self, key):
        if self.is_empty():
            return
        
        prev = None
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key:
                if prev == None:
                    self.head = self.head.get_next()
                    iter_node = iter_node.get_next()
                else:
                    prev.next = iter_node.get_next()
                    iter_node = prev.get_next()
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
    
    
    def sort(self):
        self.head = self.merge_sort(self.head)
    
    def merge_sort(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow = fast = self.head
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
        
        
        
            
            
        
        
        
    
    
    
    
    
    