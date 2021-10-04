# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:15:03 2021

@author: joaqu
"""

class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
        
    def inorder_iter(self):
        stack = []
        visited = []
        stack.append(self)
        result = []
        
        while stack:
            curr = stack.pop()
            
            if curr:
                if curr in visited:
                    result.append(curr.item)
                else:
                    stack.append(curr.right)
                    stack.append(curr)
                    stack.append(curr.left)
                    visited.append(curr)
            
        return result
    
    
    def kth_num(self, k):
        stack = []
        stack.append(self)
        
        while stack or self:
            while self:
                stack.append(self)
                self = self.left
            
            self = stack.pop()
            
            k -= 1
            if k == 0:
                return self.item
            
            self = self.right
            
            
    def lowest_common_anccestor(self, integer1, integer2):
        if self == None or self.item == None:
            return
        
        if self.item < min(integer1, integer2):
            return BST.lowest_common_anccestor(self.right, integer1, integer2)
        
        elif self.item > max(integer1, integer2):
            return BST.lowest_common_anccestor(self.left, integer1, integer2)
        
        return self.item
    
    
    def height(self):
        if self == None or self.item == None:
            return 0
        
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left, right)
        
        if left>right:
            return left + 1
        
        return right + 1
    
    
    def build_BST(self, list1):
        if len(list1) < 1:
            return
        
        mid = len(list1) // 2
        
        self = BST(list1[mid] )
        
        self.left = BST.build_BST(self.left, list1[:mid] )
        self.right = BST.build_BST(self.right, list1[mid+1:] )
        
        return self
    
        
        
        
        
        