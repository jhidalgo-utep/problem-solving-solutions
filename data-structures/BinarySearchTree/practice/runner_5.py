# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:09:28 2021

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
            if self.get_item() < new_item:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    BST.insert(self.right, new_item)
            else:
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    BST.insert(self.left, new_item)
    
    def display(self, space):
        if self == None or self.get_item() == None:
            return
        BST.display(self.right, space + '   ')
        print(space, self.get_item() )
        BST.display(self.left, space + '   ')
    
    
    def depth_of_item(self, key):
        
        if self == None or self.get_item() == None:
            return -1

        if self.get_item() == key:
            return 0
        
        if self.get_item() < key:
            d = BST.depth_of_item(self.right, key)
        else:
            d = BST.depth_of_item(self.left, key)
        
        if d < 0:
            return -1
        return d + 1
    
    
    def build_BST(self, list1):
        if len(list1) == 0:
            return
        
        mid_index = len(list1) // 2
        
        self = BST(list1[mid_index] )
        self.left = BST.build_BST(self.left, list1[:mid_index] )
        self.right = BST.build_BST(self.right, list1[mid_index+1:] )
        return self
        
    
    def height(self):
        if self == None or self.get_item() == None:
            return 0
        
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left,right)
        
        if left > right:
            return left + 1
        return right + 1
    
    def lowest_common_ancestor(self, integer1, integer2):
        if self == None or self.get_item() == None:
            return
        
        if self.get_item() < min(integer1,integer2):
            return BST.lowest_common_ancestor(self.right, integer1, integer2)
        
        elif self.get_item() > max(integer1, integer2):
            return BST.lowest_common_ancestor(self.left, integer1, integer2)
        
        return self.get_item()
    
    
    def kth_num(self, k):
        stack = []
        stack.append(self)
        
        while stack or self != None:
            while self:
                stack.append(self)
                self = self.left
            
            self = stack.pop()
            k -= 1
            if k == 0:
                return self.get_item()
            
            self = self.right
            
            
    def inorder_iter(self):
        stack = []
        visited = []
        result = []
        
        stack.append(self)
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    result.append(curr.get_item() )
                else:
                    visited.append(curr)
                    stack.append(curr.right)
                    stack.append(curr)
                    stack.append(curr.left)
        return result
        
    
    

if __name__ == "__main__":
    print('start\n')
    b = BST()
    
    b.insert(60)
    b.insert(32)
    b.insert(20)
    b.insert(40)
    b.insert(80)
    b.insert(78)
    b.display('')
    print()
    print(b.depth_of_item(25) )
    print( b.height() )
    print( b.lowest_common_ancestor(33, 31) )
    print( b.kth_num(5) )
    inorder_b = b.inorder_iter()
    print('b:', inorder_b)
    
    print()
    
    
    n = [2,3,4,6,7,9,16,24,34,62,90]
    t = BST.build_BST(None, n)
    t.display('')
    
    
        
    
        
    