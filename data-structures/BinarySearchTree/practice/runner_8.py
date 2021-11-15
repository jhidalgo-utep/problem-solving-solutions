# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:08:16 2021

@author: joaqu
"""

class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
        
    
    def insert(self, new_item):
        if self.item == None:
            self.item = new_item
        else:
            if self.item > new_item:
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
        if self == None or self.item == None:
            return
        BST.display(self.right, space+'   ')
        print(space, self.item)
        BST.display(self.left, space+'   ')
        
    
    def invert(self):
        if self == None or self.item == None:
            return
        temp = self.left
        self.left = self.right
        self.right = temp
        
        BST.invert(self.left)
        BST.invert(self.right)
        
    
    def find_common_ancestor(self, integer1, integer2):        
        if self.item > max(integer1, integer2):
            return BST.find_common_ancestor(self.left, integer1, integer2)
        
        elif self.item < min(integer1, integer2):
            return BST.find_common_ancestor(self.right, integer1, integer2)
        
        return self.item
    
    
    def preorder_iter(self):
        stack = []
        visited = []
        res = []
        stack.append(self)
        while stack:
            cur = stack.pop()
            if cur:
                if cur in visited:
                    res.append(cur.item)
                else:
                    stack.append(cur.right)
                    stack.append(cur.left)
                    stack.append(cur)
                    visited.append(cur)
        return res
    
    
    def inorder_iter(self):
        stack = []
        visited = []
        res = []
        stack.append(self)
        while stack:
            cur = stack.pop()
            if cur:
                if cur in visited:
                    res.append(cur.item)
                else:
                    stack.append(cur.right)
                    stack.append(cur)
                    stack.append(cur.left)
                    visited.append(cur)
        return res
    
    
    def kth_num(self, k):
        stack = []
        
        while stack or self:
            
            while self:
                stack.append(self)
                self = self.left
                
            self = stack.pop()
            
            k -= 1
            if k == 0:
                return self.item
            
            self = self.right
            
    
    def height(self):
        if self == None or self.item == None:
            return 0
        
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left, right)
        
        if left > right:
            return left + 1
        return right + 1
    
    
    def build_BST(self, l1):
        if len(l1) == 0:
            return
        
        mid = len(l1) // 2
        
        root = BST(l1[mid])
        root.left = BST.build_BST( None, l1[:mid] )
        root.right = BST.build_BST( None, l1[mid+1:] )
        return root
    
    
    def extract_to_list(self, l1):
        if self == None:
            return
        BST.extract_to_list(self.left)
        l1.append(self.item)
        BST.extract_to_list(self.right)
        
        
    def print_at_depth(self, d):
        if self == None:
            return
        if d == 0:
            print(self.item)
        
        BST.print_at_depth(self.left, d-1)
        BST.print_at_depth(self.right, d-1)
    
    def find(self, key):
        if self == None:
            return False
        if key == self.item:
            return True
        
        if self.item > key:
            return BST.find(self.left, key)
        else:
            return BST.find(self.right, key)
    
    
    def find_depth_of_item(self, key):
        if self == None:
            return -1
        
        if self.item == key:
            return 0
        
        if self.item > key:
            d = BST.find_depth_of_item(self.left, key)
        else:
            d = BST.find_depth_of_item(self.right, key)
        
        if d < 0 :
            return -1
        return d+1
    
    def largest(self):
        if self == None:
            return None
        
        if self.right == None:
            return self.item
        
        return BST.largest(self.right)
    
    
    def sum_at_depth(self, d):
        if self == None:
            return 0
        
        if d == 0:
            return self.item
        
        return BST.sum_at_depth(self.left, d-1) + BST.sum_at_depth(self.right, d-1)
    
    
        
        
        
        
        
        
        
    
            
            
        
if __name__ == "__main__":
    print('start\n')
    
    b = BST()
    b.insert(50) 
    b.insert(75) 
    b.insert(25) 
    b.insert(31) 
    b.insert(19) 
    b.insert(82) 
    b.insert(3) 
    b.display('') 
    
    print( b.find_common_ancestor(31, 1) )
    
    n1 = [1,2,3,4,5,6,7]
    t = BST.build_BST(None, n1)
    t.display('')

    
    
    
        
        
        