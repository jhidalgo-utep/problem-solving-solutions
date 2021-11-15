# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:43:03 2021

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
        if self.is_empty():
            return
        
        slow = fast = self.head 
        for i in range(n):
            fast = fast.get_next()
            print(i)
            if fast == None and i != n-1:
                return
            
        if fast == None:
            self.head = self.head.get_next()
            return
            
        while fast.get_next():
            slow = slow.get_next()
            fast = fast.get_next()
        
        next_node = slow.get_next().get_next()
        slow.next = next_node
        if next_node == None:
            self.tail = slow
    
    def remove_duplicates(self, key):
        if self.is_empty():
            return
        
        iter_node = self.head
        prev = None
        
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
        if list1 == None or list2 == None:
            return
        
        len1 = len2 = 0
        l1 = list1.head
        l2 = list2.head
        
        while l1:
            len1+= 1
            l1 = l1.get_next()
        
        while l2:
            len2+= 1
            l2 = l2.get_next()
        
        l1 = list1.head
        l2 = list2.head
        
        for i in range(abs(len1-len2)):
            if len1 > len2:
                l1 = l1.get_next()
            else:
                l2 = l2.get_next()
        
        while l1.get_item() != l2.get_item():
            l1 = l1.get_next()
            l2 = l2.get_next()
            if l1 == None or l2 == None:
                return
        
        return l1.get_item()


    def start_of_cycle(self):
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
            while fast != slow:
                slow = slow.get_next()
                fast = fast.get_next()
                
            return slow.get_item()
    
    def even_odd_list(self):
        if self.is_empty() or self.head.get_next() == None:
            return
        
        odd = self.head
        even = odd.get_next()
        even_head = even
        
        while even and odd and even.get_next() and odd.get_next():
            odd.next = even.get_next()
            odd = odd.get_next()
            even = odd.get_next()
            even = even.get_next()
            
        odd.next = even_head
    
    def is_palindrome(self):
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
            prev = iter_node
            slow = next_node
        
        slow = self.head
        
        while prev:
            if slow.get_item() != prev.get_item():
                return False
            slow = slow.get_next()
            fast = fast.get_next()
        
        return True
    
    
    def rotate_list(self, k):
        if self.is_empty() or k == 0:
            return 

        list_len = 0
        iter_node = self.head
        while iter_node.get_next():
            list_len+= 1
            iter_node= iter_node.get_next()
        list_len +=1
        
        k = k % list_len
        if k == 0:
            return
        
        iter_node.next = self.head
        iter_node = self.head
        
        for i in range(list_len - k - 1):
            iter_node = iter_node.get_next()
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.head = next_node
        self.tail = iter_node
    
    
    def sum_list(self, list1, list2):
        carry = 0
        l1 = list1.head
        l2 = list2.head
        res_head = temp = Node(-1)
        while l1 and l2 and carry:
            v3 = 0
            if l1:
                v3 += l1.get_item()
                l1 = l1.get_next()
            if l2:
                v3 += l2.get_item()
                l2 = l2.get_next()
            
            v3 += carry
            temp.next = Node(v3 % 10)
            carry = v3 // 10
            temp = temp.get_next()
        
        return res_head.get_next()
    
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
        elif right == None:
            return left
        
        result = None
        
        if left.get_item() < right.get_item():
            result = left
            result.next = self.merge(left.get_next(), right)
        else:
            result = right
            right.next = self.merge(left, right.get_next() )
        
        return result


def merge_sort2(node):
    if node == None or node.get_next() == None:
        return node
    
    slow = fast = node
    while fast.get_next() and fast.get_next().get_next():
        slow = slow.get_next()
        fast = fast.get_next()
    
    after_mid = slow.get_next()
    slow.next = None
    
    left = merge_sort2(node)
    right = merge_sort2(after_mid)
    return merge2(left,right)


def merge2(left, right):
    holder = temp = Node(-1)
    
    while left and right:
        if left.get_item() < right.get_item():
            temp.next = left
            left = left.get_next()
        else:
            temp.next = right
            right = right.get_next()
        temp = temp.get_next()
    
    while left:
        temp.next = left
        left = left.get_next()
        temp = temp.get_next()
    
    while right:
        temp.next = right
        right = right.get_next()
        temp = temp.get_next()
    
    return holder.get_next()
            
            
        
        
    
        
        
if __name__ == "__main__":
    print('start\n')
    ll = LinkedList()
    # ll.insert(29)
    # ll.insert(35)
    ll.insert(10)
    ll.insert(98)
    ll.display()
    ll.insert_at_start(99)
    ll.insert_after(70, 10)
    ll.insert(3)
    ll.display()    
    ll.delete(3)
    ll.display()
    ll.insert(21)
    ll.display()
    
    
    ll.remove_nth(5)
    ll.display()