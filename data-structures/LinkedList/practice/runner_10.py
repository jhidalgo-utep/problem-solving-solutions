# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:12:56 2021

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
    
    def insert_at_start(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item, old_head)
            self.head = insertee
    
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
    
    
    def delete(self, key):
        if self.is_empty() == None:
            return
        
        if self.head.get_item() == key:
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
            
    def reverse(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        iter_node = old_head = self.head
        prev = None
        while iter_node:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
        
        self.head = prev
        self.tail = old_head
        
    
    def remove_nth(self, n):
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            if fast == None and i < n-1:
                return
            
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            fast = fast.get_next()
            slow = slow.get_next()
            
        
        slow.next = slow.get_next().get_next()
        
        
    def remove_duplicates(self, key):
        if self.is_empty():
            return 
        
        iter_node = self.head
        prev = None
        
        while iter_node:
            if iter_node.get_item() == key:
                if prev == None:
                    iter_node = iter_node.get_next()
                else:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = iter_node.get_next()
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
    
    
    def start_of_cycle(self):
        if self.is_empty():
            return
        
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
        
        if slow != fast:
            return None
        
        slow = self.head
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()
        
        return slow.get_item()
    
    
    def sort(self):
        
        
            
        
        
            
        
        
        
        
        