# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:43:21 2021

@author: joaquin
"""

from LinkedList import LinkedList
from Node import Node

#18 min old
# 22 min new

def merge_sort2(head):
    if head == None or head.get_next() == None:
        return head
    
    slow = head
    fast = slow
    
    while fast.get_next() != None and fast.get_next().get_next() != None:
        slow = slow.get_next()
        fast = fast.get_next().get_next()
    
    after_mid = slow.get_next()
    slow.next = None
    
    left = merge_sort2(head)
    right = merge_sort2(after_mid)
    return merge2(left, right)
    

def merge2(left_head, right_head):
    merged = Node(-1)
    temp = merged
    
    while (left_head != None and right_head != None):
        if (left_head.get_item() < right_head.get_item()):
            temp.next = left_head
            left_head = left_head.next
        else:
            temp.next = right_head
            right_head = right_head.next
        temp = temp.next
     
    # While head1 is not null
    while (left_head != None):
        temp.next = left_head
        left_head = left_head.next
        temp = temp.next
     
    # While head2 is not null
    while (right_head != None):
        temp.next = right_head
        right_head = right_head.next
        temp = temp.next
     
    return merged.next

if __name__ == "__main__":
    print('start program\n')
    
    ll = LinkedList()
    
    ll.insert(21)
    ll.insert(5)
    ll.insert(44)
    ll.insert(37)
    ll.insert(82)
    
    ll.display()
    
    ll.delete(82)
    ll.insert(88)
    
    ll.display()
    
    print('list length: ', ll.get_list_length())
    
    ll.reverse_list()
    ll.display()
    ll.insert(99)
    ll.insert(2)
    ll.display()
    ll.insert(77)
    ll.display()
    # ll.sort()
    # ll.display()
    # ll.insert(7)
    # ll.display()
    
    ll.head = merge_sort2(ll.head)
    ll.display()
    
    