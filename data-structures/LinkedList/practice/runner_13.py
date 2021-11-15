# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:34:57 2021

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
            
    
    def insert_at_begin(self, new_item):
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
        
    
    def remove_nth(self, n):
        if self.is_empty():
            return
        
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            if fast == None and i != n-1:
                return
        
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
        
        slow.next = slow.get_next().get_next()
        
    
    def remove_duplicates(self, key):
        if self.is_empty():
            return
        
        prev = None
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key:
                if prev == None:
                    iter_node = iter_node.get_next()
                    self.head = self.head.get_next()
                else:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = next_node
                    if next_node == None:
                        self.tail = prev
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
    
    def display(self):
        if self.is_empty():
            return
        
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end=' ')
            iter_node = iter_node.get_next()
        print()
        
        
    def sort(self):
        self.head = self.merge_sort(self.head)
        
        
    def merge_sort(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow = fast = node
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        after_mid = slow.get_next()
        slow.next = None
        
        left = self.merge_sort(node)
        right = self.merge_sort(after_mid)
        
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        if left == None:
            return right
        
        if right == None:
            return left
        
        res = None
        
        if left.item < right.item:
            res = left
            res.next = self.merge(left.get_next(), right)
        else:
            res = right
            res.next = self.merge(left, right.get_next() )
        
        return res

    def get_intersect(self, list1, list2):
        l1 = list1.head
        l2 = list2.head
        
        len1 = len2 = 0
        
        while l1:
            len1 += 1
            l1 = l1.get_next()
        
        while l2:
            len2 += 1
            l2 = l2.get_next()
        
        l1 = list1.head
        l2 = list2.head
        
        for i in range(abs(len1 - len2) ):
            if len1 > len2:
                l1 = l1.get_next()
            else:
                l2 = l2.get_next()
                
        while l1 and l2:
            if l1.get_item() == l2.get_item():
                return l1.get_item()
            l1 = l1.get_next()
            l2 = l2.get_next()
            
        return None
    
    def begin_cycle(self):
        slow = fast = self.head
        
        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
            
        if slow != fast:
            return
        
        slow = self.head
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()
        
        return slow.get_item()
    
    
    def odd_even_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        odd = self.head
        even = odd.get_next()
        even_head = even
        
        while odd and even and odd.get_next() and even.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            odd = odd.get_next()
            
        odd.next = even_head
        
    
    def is_palindrome(self):
        if self.is_empty() or self.head.get_next():
            return True
        
        slow = fast = self.head
        prev = None
        
        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        while slow:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
            
        slow = self.head
            
        while prev:
            if prev.get_item() != slow.get_item():
                return False
            prev = prev.get_next()
            slow = slow.get_next()
            
        return True
    
    
    def rotate_list(self, k):
        if k == 0:
            return 
        
        list_len = 0
        iter_node = self.head
        
        while iter_node.get_next():
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        if k % list_len == 0:
            return 
        
        iter_node.next = self.head
        iter_node = self.head
        
        for i in range( list_len - k - 1):
            iter_node = iter_node.get_next()
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.tail = iter_node
        self.head = next_node
    
    
    def add_nums(self, list1, list2):
        list1 = list1.head
        list2 = list2.head
        
        res = holder = Node(-1)
        carry = 0
        
        while list1 or list2 or carry:
            v3 = 0
            if list1:
                v3 += list1.get_item()
                list1 = list1.get_next()
            
            if list2:
                v3 += list2.get_item()
                list2 = list2.get_next()
            
            v3 += carry
            res.next = Node(v3%10)
            res = res.get_next()
            carry = v3 // 10
        
        return holder.get_next()
    
        
        
            
        
        
        
        
        
        
        
            
        
            
        
        
        
    
    
                    
                    
                    
        
        
                
        
    
    
    
    
    
    