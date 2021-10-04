# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:10:23 2021

@author: joaqu
"""
# 1hr 41 min


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
    
    def get_list_length(self):
        if self.is_empty():
            return 0
        iter_node = self.head
        result = 0
        while iter_node:
            result += 1
            iter_node = iter_node.get_next()
        return result
    
    def insert(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.get_next()
            
    def insert_at_begin(self, new_item):
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
                break
            iter_node = iter_node.get_next()
            
        if iter_node == None:
            return
        
        next_node = iter_node.get_next()
        insertee = Node(new_item)
        insertee.next = next_node
        iter_node.next = insertee
        
        if next_node == None:
            self.tail = insertee
        
    
    def reverse_list(self):
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
        
    
    def delete(self, key_item):
        if self.is_empty():
            return
        
        if self.head.get_item() == key_item:
            self.head = self.head.get_next()
            return
        
        prev = None
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key_item:
                break
            prev = iter_node
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        
        prev.next = iter_node.get_next()
        if prev.get_next() == None:
            self.tail = prev
        
    #Practice!
    def remove_nth(self, n):
        if self.is_empty():
            return
        
        slow = fast = self.head
        
        for i in range(n):
            fast = fast.get_next()
            if fast == None and i < n-1:
                return False
        
        if fast == None:
            self.head = self.head.get_next()
            return True
        
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
        
        slow.next = slow.get_next().get_next()
        
    
    def remove_duplicates(self, key_item):
        if self.is_empty():
            return
        prev = None
        iter_node = self.head
        
        while iter_node:
            if iter_node.get_item() == key_item:
                if prev == None:
                    iter_node = iter_node.get_next()
                    self.head = self.head.get_next()
                else:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = next_node
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
                
    # Practice!
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
            result.next = self.merge(left.get_next(), right )
        else:
            result = right
            result.next = self.merge(left, right.get_next() )
        return result
                
    
    def get_intersect(self, list1, list2):
        len1 = len2 = 0
        p1 = list1.head
        p2 = list2.head
        
        while p1:
            p1 = p1.get_next()
            len1 += 1
        
        while p2:
            p2 = p2.get_next()
            len2 += 1
        
        p1 = list1.head
        p2 = list2.head
        
        for i in range(abs(len1 - len2) ):
            if len1 < len2:
                p2 = p2.get_next()
            else:
                p1 = p1.get_next()
        
        while p1.get_item() != p2.get_item() and p1 and p2:
            p1 = p1.get_next()
            p2 = p2.get_next()
        
        if p1 and p2:
            return p1.get_item()
        return None
    
    
    def has_cycle(self):
        if self.is_empty():
            return False
        slow = fast = self.head
        
        while fast.get_next() and fast.get_next().get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    
    def cycle_begin(self):
        if self.is_empty():
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
        
    
    def odd_even_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        odd = self.head
        even = self.head.get_next()
        even_head = even
        
        while odd and even and odd.get_next() and even.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            
            even.next = odd.get_next()
            even = even.get_next()
        
        odd.next = even_head
        
    
    # Practice !
    def is_palindrome(self):
        if self.is_empty() or self.head.get_next() == None:
            return True
        
        slow = head = self.head
        while fast and fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        prev = None
        while slow:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
        
        start = self.head
        while prev:
            if start.get_item() != prev.get_item():
                return False
            start = start.get_next()
            prev = prev.get_next()
        return True
    
    
    # Practice!
    # you are given a list that does not have a cycle, it is a straight linked list
    def rotate_list(self, k):
        if self.is_empty or k == 0 or self.head.get_next() == None:
            return
        
        list_len = 0
        iter_node = self.head
        
        
        while iter_node.get_next():
            list_len +=1
            iter_node = iter_node.get_next()
        list_len += 1
        
        if k % list_len == 0:
            return
        
        k = k % list_len
        
        iter_node.next = self.head
        iter_node = self.head
        
        for i in range(list_len - k - 1):
            iter_node = iter_node.get_next()
            
        new_head = iter_node.get_next()
        iter_node.next = None
        self.head = new_head
        
    
    # Practice!
    def add_two_nums(self, list1, list2):
        carry = 0
        list1 = list1.head
        list2 = list2.head
        start = temp = Node(-1)
        
        while list1 or list2 or carry:
            v1 = v2 = 0
            if list1:
                v1 = list1.get_item()
                list1 = list1.get_next()
            if list2:
                v2 = list2.get_item()
                list2 = list2.get_next()
            
            v3 = v1 + v2 + carry
            temp.next = Node(v3 % 10)
            carry = v3 // 10
            temp = temp.get_next()
        
        return start.get_next()
        
        

if __name__ == "__main__":
    print('start\n')
    ll = LinkedList()
    ll.insert(45)
    ll.insert(20)
    ll.insert(33)
    ll.insert(81)
    ll.display()
    ll.remove_nth(6)
    ll.display()
    ll.sort()
    ll.display()
                