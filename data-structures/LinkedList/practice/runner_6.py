# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:09:42 2021

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
    
    def insert(self, new_item ):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item )
            self.tail = self.tail.get_next()
    
    def insert_at_start(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee = Node(new_item)
            insertee.next = old_head
            self.head = insertee
    
    def insert_after(self, new_item, key_item):
        if self.is_empty():
            return
        
        iter_node = self.head
        while iter_node:
            if iter_node.get_item() == key_item:
                next_node = iter_node.get_next()
                insertee = Node(new_item)
                iter_node.next = insertee
                if next_node == None:
                    insertee.next = None
                    self.tail = insertee
                else:
                    insertee.next = next_node
                return
            iter_node = iter_node.get_next()
            
            
    def delete(self, key_item):
        if self.is_empty():
            return
        
        if self.head.get_item() == key_item:
            self.head = self.head.get_next()
            return
        
        iter_node = self.head
        prev = None
        
        while iter_node:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
            
        
        if iter_node == None:
            return
        
        if iter_node.get_next() == None:
            prev.next = None
            self.tail = prev
        else:
            prev.next = iter_node.get_next()
            
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
        if self.is_empty():
            return
        
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
        if slow.next == None:
            self.tail = slow
        
        
    def remove_duplicates(self, key_item):
        if self.is_empty():
            return
        
        prev = None
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key_item:
                if prev:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = next_node
                else:
                    self.head = self.head.get_next()
                    iter_node = iter_node.get_next()
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
        
        for i in range(abs(len1 - len2) ):
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
            return False
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            fast = fast.get_next().get_next()
            slow = slow.get_next()
            if slow == fast:
                break
    
        if fast.get_next() == None or fast.get_next().get_next() == None:
            return False
        
        if slow == fast:
            return True
        
    def start_of_cycle(self):
        if self.is_empty() or self.head.get_next() == None:
            return False
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            fast = fast.get_next().get_next()
            slow = slow.get_next()
            if slow == fast:
                break
    
        if fast.get_next() == None or fast.get_next().get_next() == None:
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
            even = even.get_next()
        
        odd.next = even_head
        
        
    def is_palindorme(self):
        if self.is_empty() or self.head.get_next() == None:
            return True
        
        slow = self.head
        fast = slow
        
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
            if slow.get_item() != prev.get_item():
                return False
            prev = prev.get_next()
            slow = slow.get_next()
        return True
    
    
    def rotate_list(self, k):
        if self.is_empty() or self.head.get_next() == None or k == 0:
            return
        
        iter_node = self.head
        list_len = 0
        while iter_node.get_next():
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        k = k % list_len
        if k == 0:
            return
        
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
            iter_node = iter_node.get_next()
            carry = v3 // 10
        
        return holder.get_next()
    
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
        return node
    
    slow = fast = node
    
    while fast.get_next() and fast.get_next().get_next():
        slow = slow.get_next()
        fast = fast.get_next().get_next()
    
    after_mid = slow.get_next()
    slow.next = None
    
    left = merge_sort(node)
    right = merge_sort(after_mid)
    
    return merge(left, right)

def merge(left, right):
    result = Node(-1)
    while left and right:
        if left.get_item() < right.get_item():
            result.next = left
            left = left.get_next()
        else:
            result.next = right
            right = right.get_next()
        
        result = result.get_next()
    
    while left:
        result.next = left
        left = left.get_next()
    
    while right:
        result.next = right
        right = right.get_next()
    
    return result.get_next()
            
        
        
        
            


if __name__ == "__main__":
    print('start\n')
    ll = LinkedList()
    ll.insert_at_start(80)
    ll.insert(54)
    ll.insert_at_start(12)
    ll.insert(100)
    ll.insert(50)
    ll.insert_after(37, 50)
    ll.display()
    ll.insert(59)
    ll.insert(20)
    ll.insert(75)
    ll.display()
    ll.rotate_list(10)
    ll.display()
    ll.sort()
    ll.display()