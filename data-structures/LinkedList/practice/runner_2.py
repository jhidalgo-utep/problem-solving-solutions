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
    
    # 5 - 10 - 7 - 13
    def insert_after(self, key_item, new_item):
        if self.is_empty():
            return
        iter_node = self.head
        while iter_node != None:
            if iter_node.get_item() == key_item:
                break
            iter_node = iter_node.get_next()
        
        if iter_node == None:
            return
        next_node = iter_node.get_next()
        insertee_node = Node(new_item, next_node)
        iter_node.next = insertee_node
        if next_node == None:
            self.tail = insertee_node
    
    def insert_at_begin(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
        else:
            old_head = self.head
            insertee_node = Node(new_item, old_head)
            self.head = insertee_node
            
    
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
            
    # given: [ 8 - 3 - 6 - 9 - 5] and nth: 3.  Result is: [ 8 - 3 - 9 - 5]
    def remove_nth_node(self, nth):
        slow = fast = self.head
        
        for i in range(nth):
            fast = fast.get_next()
        
        if fast == None:
            self.head = self.head.get_next()
            return
        
        while fast.get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next()
        
        slow.next = slow.get_next().get_next()
        
        
    # NEEDS TESTING but works on leetcode
    def remove_duplicates(self, key_item):
        iter_node = self.head
        prev = None
        while iter_node != None:
            if iter_node.get_item() == key_item:
                if prev != None:
                    next_node = iter_node.get_next()
                    prev.next = next_node
                    iter_node = next_node
                else:
                    self.head = self.head.next
                    iter_node = iter_node.get_next()
            else:
                prev = iter_node
                iter_node = iter_node.get_next()
        
            
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
        
        
    #assuming there is an intersection
    # NEEDS TESTING but works on leetcode
    def get_list_intersect(self, list1, list2):
        pointer1 = list1.head
        pointer2 = list2.head
        len1 = len2 = 0
        
        while pointer1 != None:
            len1 += 1
            pointer1 = pointer1.get_next()
        while pointer2 != None:
            len2 += 1
            pointer2 = pointer2.get_next()
        
        pointer1 = list1.head
        pointer2 = list2.head
        
        for i in range( abs(len1 - len2) ):
            if len1 > len2:
                pointer1 = pointer1.get_next()
            else:
                pointer2 = pointer2.get_next()
        
        while pointer1 != pointer2:
            pointer1 = pointer1.get_next()
            pointer2 = pointer2.get_next()
            
        return pointer1.get_item()
    
    
    # NEEDS TESTING but works on leetcode
    def has_cycle(self):
        if self.head == None or self.head.get_item() == None:
            return False
        
        slow = self.head
        fast = slow
        
        while fast.get_next() != None and fast.get_next().get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                return True
        return False
    
    
    # NEEDS TESTING but works on leetcode
    def has_cycle_get_start_of(self):
        if self.head == None or self.head.get_item() == None:
            return None
        
        slow = self.head
        fast = slow
        
        while fast.get_next() != None and fast.get_next().get_next() != None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            if slow == fast:
                break
        
        if fast.get_next() == None or fast.get_next().get_next() == None:
            return None
        temp = self.head
        while temp != slow:
            temp = temp.get_next()
            slow = slow.get_next()
        return slow.get_item()
    
    # NEEDS TESTING but works on leetcode
    def odd_even_index_list(self):
        if self.head == None:
            return 
        
        odd = self.head
        even = self.head.get_next()
        even_head = even
        while odd != None and even != None and even.next != None and odd.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return 
    
    
    # NEEDS TESTING but works on leetcode
    def is_palindrome(self):
        if self.head.get_next() == None:
            return True
        
        fast = slow = self.head
        
        while fast != None and fast.get_next() != None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow != None:
            next_node = slow.get_next()
            slow.next = prev
            prev = slow
            slow = next_node
        
        left = head
        right = prev
        
        while right:
            if left.get_item() != right.get_item():
                return False
            left = left.get_next()
            right = right.get_next()
        return True
    
    
    # NEEDS TESTING but works on leetcode
    def rotate_list(self, n):
        if self.head == None or self.head.get_next() == None or n == 0:
            return
        
        iter_node = self.head
        list_len = 0
        while iter_node.get_next() != None:
            list_len += 1
            iter_node = iter_node.get_next()
        list_len += 1
        
        rotate_num = n % list_len
        if rotate_num == 0:
            return 
        
        iter_node.next = self.head
        
        iter_node = self.head
        i = 0
        while i < list_len - 1 - rotate_num:
            iter_node = iter_node.get_next()
            i += 1
        
        next_node = iter_node.get_next()
        iter_node.next = None
        self.head = next_node
        
        
    # NEEDS TESTING but works on leetcode
    def add_two_nums(self, list1, list2):
        carry = 0
        place_holder = iter_node = Node(-1)
        
        while list1 or list2 or carry:
            v1 = v2 = 0
            if list1:
                v1 = list1.get_item()
                list1 = list1.get_next()
            if list2:
                v2 = list2.get_item()
                list2 = list2.get_next()
            
            insertee = v1+v2+carry
            iter_node.next = Node(insertee % 10)
            carry = insertee // 10
            iter_node = iter_node.next
            
        return place_holder.next
    
    # NEEDS TESTING but works on leetcode
    def merge_two_lists(self, list1, list2):
                
        if not list1 or not list2:
            return list1 or list2
        
        if list1.get_item() < list2.get_item():
            list1.next = self.mergeTwoLists(list1.get_next(), list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.get_next() )
            return list2
        
        
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
    print('list len: ', ll.get_list_length() , '\n')
    ll.insert(100)
    ll.display()
    ll.remove(100)
    ll.insert(777)
    ll.display()
    ll.reverse()
    ll.display()
    ll.insert(18)
    ll.display()
    ll.insert_after(18, 11)
    ll.display()
    ll.insert(99)
    ll.display()
    ll.insert_at_begin(4)
    ll.display()
    ll.insert(91)
    ll.display()
    ll.remove_nth_node(1)
    ll.display()
    
    
    # ll.head = merge_sort(ll.head) #  option 1
    # #ll.sort()  #  option 2
    # ll.display()
    
    