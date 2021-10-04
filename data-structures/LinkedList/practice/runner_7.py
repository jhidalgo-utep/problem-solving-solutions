# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:52:37 2021

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
    
    def display(self):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node:
            print(iter_node.get_item(), end = ' ')
            iter_node = iter_node.get_next()
        print()
    
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
        if self.is_empty():
            return
        
        if self.head.get_item() == key:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        prev = None
        while iter_node:
            if iter_node.get_item() == key:
                next_node = iter_node.get_next()
                prev.next = next_node
                if next_node == None:
                    self.tail = prev
                return
            prev = iter_node
            iter_node = iter_node.get_next()
        
    
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
    
    
    def remove_nth(self, k):
        if self.is_empty():
            return
        
        slow = fast = self.head
        
        for i in range(k):
            fast = fast.get_next()
            if fast == None and i < k-1:
                return
        
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next():
            fast = fast.get_next()
            slow = slow.get_next()
        
        slow.next = slow.get_next().get_next()
        
        if slow.get_next() == None:
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
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = next_node
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
    
    def get_intersect(self, list1, list2):
        len1 = len2 = 0
        p1 = list1.head
        p2 = list2.head
        
        while p1:
            len1 += 1
            p1 = p1.get_next()
        while p2:
            len2 += 1
            p2 = p2.get_next()
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range( abs(len1-len2) ):
            if len1 > len2:
                p1 = p1.get_next()
            else:
                p2 = p2.get_next()
        
        while p1.get_item() != p2.get_item():
            p1 = p1.get_next()
            p2 = p2.get_next()
            if p1 == None or p2 == None:
                return
        return p1.get_item()
    
    
    def is_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    
    def start_of_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        slow = fast = self.head
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
        
        if slow == fast:
            slow = self.head
            while slow != fast:
                slow = slow.get_next()
                fast = fast.get_next()
            return slow.get_item()
        return
    
    
    def even_odd_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        odd = self.head
        even = odd.get_next()
        even_head = even
        
        while odd and even and odd.get_next() and even.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
        
    
    def is_palidrone(self):
        if self.is_empty() or self.head.get_next() == None:
            return True
        
        slow = fast = self.head
        
        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        prev = None
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
        if self.is_empty() or k == 0:
            return
        
        list_len = 0
        iter_node = self.head
        while iter_node.get_next():
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        if k % list_len == 0:
            return
        
        k = k % list_len
        
        iter_node.next = self.head
        iter_node = self.head
        
        for i in range( list_len - 1 - k):
            iter_node = iter_node.get_next()
            
        next_node = iter_node.get_next()
        self.head = next_node
        iter_node.next = None
        self.tail = iter_node
        
    
    def sum_list(self, list1, list2):
        carry = 0
        list1 = list1.head
        list2 = list2.head
        holder = iter_node = Node(-1)
        
        while list1 or list2 or carry:
            v3 = 0
            if list1:
                v3 += list1.get_item()
                list1 = list1.get_next()
            if list2:
                v3 += list2.get_item()
                list2 = list2.get_next()
            
            v3 += carry
            iter_node.next = Node(v3 % 10)
            carry = v3 // 10
            iter_node = iter_node.get_next()
        return holder.get_next()
    
    
    def sort(self):
        self.head = self.merge_sort(self.head)
        
        
    def merge_sort(self, node):
        if node == None or node.get_next() == None:
            return node
        
        slow  = fast = node
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
        after_mid = slow.get_next()
        slow.next = None
        
        left = self.merge_sort(node)
        right = self.merge_sort(after_mid)
        
        return self.merge(left,right)
    
    
    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        
        result = None
        if left.get_item() < right.get_item():
            result = left
            result.next = self.merge(left.get_next(), right)
        else:
            result = right
            result.next = self.merge(left, right.get_next() )
            
        return result
    

def merge_sort2(node):
    if node == None or node.get_next() == None:
        return
    
    slow  = fast = node
        
    while fast.get_next() and fast.get_next().get_next():
        slow = slow.get_next()
        fast = fast.get_next().get_next()
        
    after_mid = slow.get_next()
    slow.next = None
    
    left = merge_sort2(node)
    right = merge_sort2(after_mid)
    
    return merge(left,right)

def merge(left, right):
    holder = iter_node = Node(-1)
    
    while left and right:
        if left.get_item() < right.get_item():
            iter_node.next = left
            left = left.get_next()
        else:
            iter_node.next = right
            right = right.get_next()
        iter_node = iter_node.get_next()
    
    while left:
        iter_node.next = left
        left = left.get_next()
        iter_node = iter_node.get_next()
        
    while right:
        iter_node.next = right
        right = right.get_next()
        iter_node = iter_node.get_next()
    
    return holder.get_next()
            
        
        
            
        
        
    
            

if __name__ == "__main__":
    print('start\n')
    ll = LinkedList()
    ll.insert(77)
    ll.insert(30)
    ll.insert_at_start(11)
    ll.insert(40)
    ll.insert_after(20, 40)
    ll.insert(31)
    ll.display()
    ll.delete(20)
    ll.insert(88)
    ll.display()
    ll.remove_nth(6)
    ll.insert(55)
    
    ll.display()
    ll.rotate_list(1)
    ll.display()
    ll.sort()
    ll.display()