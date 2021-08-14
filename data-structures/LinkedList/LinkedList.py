# -*- coding: utf-8 -*-
"""
Created on Tue May 27 21:34:02 2021

@author: joaquin
"""

from Node import Node

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
        if self == None or self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()

    def get_list_length(self):
        if self.is_empty():
            return 0
        result = 0
        iter_node = self.head
        while iter_node != None:
            result += 1
            iter_node = iter_node.get_next()
        return result
    
    def get_middle_index(self):
        if self == None:
            return -1
        list_len = self.get_list_length()
        if list_len < 2:
            return 0
        
        if list_len % 2 == 0:
            return ( list_len // 2 ) - 1
        else:
            return list_len // 2
    

    def reverse_list(self):
        if self == None or self.is_empty():
            return
        if self.head.get_next() == None:
            return
        
        prev = None
        curr_node = self.head
        soon_to_be_tail_node = curr_node # save our head, this will be our tail after reverse
        
        while curr_node != None:
            next_node = curr_node.get_next()
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
            
        #update head and tail
        self.head = prev
        self.tail = soon_to_be_tail_node
        

    def delete(self, key_item):
        if self == None or self.is_empty():
            return
        
        #check head node for key_item
        if self.head.get_item() == key_item:
            self.head = self.head.get_next()
            # if self.head == None or self.head.get_next() == None:
            #     self.tail = self.head
            return
        
        iter_node = self.head
        while iter_node != None:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        
        prev.next = iter_node.get_next()
        if prev.get_next() == None:
            self.tail = prev    
            
    def sort(self):
        self.head = self.merge_sort(self.head)
        
    def merge_sort(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow = node
        fast = slow
        while fast.next != None and fast.next.next != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
        after_mid = slow.next
        slow.next = None
        left = LinkedList.merge_sort(None, node)
        right = LinkedList.merge_sort(None, after_mid)
        return LinkedList.merge(None, left, right)
    
    def merge(self, left_head, right_head):
        if left_head == None:
            return right_head
        if right_head == None:
            return left_head
        result = None
        
        if left_head.get_item() < right_head.get_item():
            result = left_head
            result.next = LinkedList.merge(None, left_head.get_next(), right_head)
        else:
            result = right_head
            result.next = LinkedList.merge(None, left_head, right_head.get_next() )
        return result
        
    
        