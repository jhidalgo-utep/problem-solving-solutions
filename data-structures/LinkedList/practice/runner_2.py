# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:33:22 2021

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
        while iter_node != None:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print('\n')
    
    def remove(self, key_item):
        if self.is_empty():
            return
        
        if self.head.get_item() == key_item:
            self.head = self.head.get_next()
        
        iter_node = self.head
        prev = None
        while iter_node != None:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        
        prev.next = iter_node.get_next()
        
        if prev.next == None:
            self.tail = prev
            
    def reverse(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        iter_node = self.head
        soon_to_be_tail = self.head
        prev = None
        
        while iter_node != None:
            next_node = iter_node.get_next()
            iter_node.next = prev
            prev = iter_node
            iter_node = next_node
        
        self.head = prev
        self.tail = soon_to_be_tail
        
        
    # ### PRACTICE (small adjustment) ###
    def sort(self):
        self.head = self.merge_sort2(self.head)
        
    def merge_sort2(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow = node
        fast = slow
        
        while fast.get_next() != None and fast.get_next().get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        after_mid = slow.next
        slow.next = None
        
        left = LinkedList.merge_sort2(None, node)
        right = LinkedList.merge_sort2(None, after_mid)
        return LinkedList.merge2(None, left, right)
    
    def merge2(self, left_head, right_head):
        
        
        if left_head == None:
            return right_head
        if right_head == None:
            return left_head
        
        result = None

        if left_head.get_item() < right_head.get_item():
            result = left_head
            result.next = LinkedList.merge2(None, left_head.get_next(), right_head)
        else:
            result = right_head
            result.next = LinkedList.merge2(None, left_head, right_head.get_next() )
        return result
    
    def get_list_length(self):
        if self.is_empty():
            return 0
        iter_node = self.head
        result = 0
        while iter_node != None:
            result += 1
            iter_node = iter_node.get_next()
        return result
            

            
        
        
# ### PRACTICE (small adjustment) ###
def merge_sort(head):
    if head == None or head.get_next() == None:
        return head
    
    slow = head
    fast = slow
    
    while fast.get_next() != None and fast.get_next().get_next() != None:
        slow = slow.get_next()
        fast = fast.get_next().get_next()
    
    after_mid = slow.get_next()
    slow.next = None
    
    left = merge_sort(head)
    right = merge_sort(after_mid)
    return merge(left, right)

def merge(left_head, right_head):
    start_of_list = Node(-1)
    iter_node = start_of_list
    
    while left_head != None and right_head != None:
        if left_head.get_item() < right_head.get_item():
            iter_node.next = left_head
            left_head = left_head.get_next()
        else:
            iter_node.next = right_head
            right_head = right_head.get_next()
        iter_node = iter_node.get_next()
    
    while left_head != None:
        iter_node.next = left_head
        left_head = left_head.get_next()
        iter_node = iter_node.get_next()
    
    while right_head != None:
        iter_node.next = right_head
        right_head = right_head.get_next()
        iter_node = iter_node.get_next()
    
    return start_of_list.next
    
        

if __name__ == "__main__":
    print('start program\n')
    ll = LinkedList()
    ll.insert(24)
    ll.insert(77)
    ll.insert(81)
    ll.insert(42)
    ll.insert(10)
    ll.insert(5)
    ll.insert(60)
    ll.display()
    ll.remove(5)
    ll.display()
    ll.insert(100)
    ll.display()
    ll.remove(100)
    ll.insert(777)
    ll.display()
    ll.reverse()
    ll.display()
    ll.insert(18)
    ll.display()
    print('list len: ', ll.get_list_length() , '\n')
    
    ll.head = merge_sort(ll.head)
    # ll.sort()
    ll.display()
    
    