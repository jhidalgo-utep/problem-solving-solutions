# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:16:18 2021

@author: joaqu
"""

class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_next_node(self):
        return self.next
    
    def get_item(self):
        return self.item

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get_tail_node(self):
        return self.tail
    
    def set_tail_node(self, new_node):
        self.tail = new_node
        
    def is_empty(self):
        return self.head == None
        
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.get_tail_node().next = Node(new_item)
            self.set_tail_node(self.get_tail_node().get_next_node())
            
    def get_list_length(self):
        if self.is_empty():
            return 0
        list_length = 0
        iter_node = self.head
        while iter_node != None:
            list_length += 1
            iter_node = iter_node.get_next_node()
        return list_length
            
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_item() )
            iter_node = iter_node.get_next_node()
            
    
    def get_middle_index(self):
        if self.is_empty():
            return -1
        length_of_list = self.get_list_length()
        if length_of_list < 2:
            return 0
        if length_of_list % 2 == 0:
            return (length_of_list // 2)- 1
        return length_of_list //2
    
    def remove_node(self, key_item):
        if self.is_empty():
            return
        
        iter_node = self.head
        
        #checks for key_item @ the head
        if iter_node.get_item() == key_item:
            self.head = iter_node.get_next_node()
            return
        
        #Iterate till found or at end of LL
        while iter_node != None:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next_node()
        
        #Item not found in LL
        if iter_node == None:
            return
        
        prev.next = iter_node.get_next_node()
        


if __name__ == "__main__":
    print('start program\n')
    ll = LinkedList()
    ll.insert(21)
    ll.insert(6)
    ll.insert(53)
    ll.insert(77)
    ll.insert(99)
    ll.display()
    print('\nlength:', ll.get_list_length())
    print(ll.get_middle_index() )
        