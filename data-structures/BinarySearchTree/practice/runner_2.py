# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:50:10 2021

@author: joaqu
"""

class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
        
    def get_item(self):
        return self.item
    
    def insert(self, new_item):
        if self.item == None:
            self.item = new_item
        else:
            if new_item < self.get_item():
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    BST.insert(self.left, new_item)
            else:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    BST.insert(self.right, new_item)
    
    def display(self, space):
        if self == None:
            return
        BST.display(self.right, space + '   ')
        print(space, self.get_item() )
        BST.display(self.left, space + '   ')
        
    
    def height(self):
        if self == None or self.item == None:
            return 0
        
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left, right)
        
        if left> right:
            return left + 1
        return right + 1
    
    # ### PRACTICE (small adjustment) ###
    def build_BST(self, L):
        if L == None or len(L) == 0:
            return
        mid = len(L) // 2
        self = BST( L[mid] )
        self.left = BST.build_BST( None, L[:mid] )
        self.right = BST.build_BST( None, L[mid+1:] )
        return self
    
    
    # ### PRACTICE (small adjustment) ###
    def find_depth_of_item(self, key_item):
        if self == None or self.item == None:
            return -1
        
        elif self.get_item() == key_item:
            return 0
        
        if key_item < self.get_item():
            d = BST.find_depth_of_item(self.left, key_item)
        else:
            d = BST.find_depth_of_item(self.right, key_item)
        
        if d < 0:
            return -1
        return d + 1
    
    def sum_at_depth(self, depth):
        if self == None or self.item == None:
            return 0
        if depth == 0:
            return self.get_item()
        return BST.sum_at_depth(self.left, depth - 1) + BST.sum_at_depth(self.right, depth - 1)
    
    def find(self, key_item):
        if self == None or self.get_item() == None:
            return False
        if key_item == self.get_item():
            return True
        if key_item < self.get_item():
            return BST.find(self.left, key_item)
        return BST.find(self.right, key_item)
    
    def extract_to_list(self, L):
        if self == None or self.item == None:
            return
        BST.extract_to_list(self.left, L)
        L.append(self.item)
        BST.extract_to_list(self.right, L)
    
    
    # NEEDS TESTING but works on leetcode
    def lowest_common_ancestor(self, integer1, integer2):
        if self == None or self.item == None:
            return
        elif self.item > max(integer1, integer2):
            return BST.lowest_common_ancestor(self.left, integer1, integer2)
        elif self.item < min(integer1, integer2):
            return BST.lowest_common_ancestor(self.right, integer1, integer2)
        return self.item
    
    
    # NEEDS TESTING but works on leetcode
    # Instead of self, root is a parameter and is used in the code below in leetcode
    def kth_num(self, k):
        stack = []
        while stack or self.item:
            while self.item:
                stack.append(self)
                self = self.left
            self = stack.pop()
            k -= 1
            if k == 0:
                return self.item
            self = self.right
    
        
        

if __name__ == "__main__":
    print('start program\n')
    b = BST()
    b.insert(50)
    b.insert(75)
    b.insert(69)
    b.insert(85)
    b.insert(25)
    b.insert(31)
    b.insert(5)
    b.insert(1)
    b.insert(30)
    b.display(' ')
    
    print('\n')
    print('height: ', b.height() )
    print('find depth of 85:', b.find_depth_of_item(85) )
    print('sum at depth 1:', b.sum_at_depth(1) )
    print('find 30:', b.find(30) )
    w = []
    b.extract_to_list(w)
    print(w)
    
    
    
    # n = [1, 4, 7, 10, 19, 25, 44, 59, 78, 100]
    # d = BST.build_BST(None, n)
    # d.display(' ')
    