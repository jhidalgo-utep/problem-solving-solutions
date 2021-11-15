# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:14:31 2021

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
        if self == None:
            return
        BST.display(self.right, space+'  ' )
        print(space, self.item)
        BST.display(self.left, space+'  ' )
        
    
    def sum_at_depth(self, d):
        if self == None:
            return 0
        elif d == 0:
            return self.item
        
        return BST.sum_at_depth(self.left, d-1) + BST.sum_at_depth(self.right, d-1)
    
    
    def find_depth_of_item(self, key):
        if self == None:
            return -1
        elif self.item == key:
            return 0
        
        if self.item > key:
            d = BST.find_depth_of_item(self.left, key)
        else:
            d = BST.find_depth_of_item(self.right, key)
        
        if d < 0:
            return -1
        return d + 1
        
    def smallest(self):
        if self.item == None:
            return None
        elif self.left == None:
            return self.item
        return BST.smallest(self.left)
    
    def largest(self):
        if self.item == None:
            return None
        elif self.right == None:
            return self.right
        return BST.largest(self.right)
    
    def find(self, key):
        if self == None:
            return
        elif self.item == key:
            return True
        
        if self.item > key:
            return BST.find(self.left, key)
        return BST.find(self.right, key)
    
    def print_at_depth(self, d):
        if self == None:
            return
        elif d == 0:
            print(self.item, end = ' ')
        BST.print_at_depth(self.left, d-1)
        BST.print_at_depth(self.right, d-1)
    
    def sum_of_nodes(self):
        if self == None:
            return 0
        return self.item + BST.sum_of_nodes(self.left) + BST.sum_of_nodes(self.right)
    
    def num_of_nodes(self):
        if self == None:
            return 0
        return 1 + BST.num_of_nodes(self.left) + BST.num_of_nodes(self.right)
    
    def extract_to_list(self, l1):
        if self == None:
            return
        BST.extract_to_list(self.left, l1 )
        l1.append(self.item )
        BST.extract_to_list(self.right, l1 )
    
    def build_BST(self, l1):
        if len(l1) < 1:
            return
        
        mid = len(l1) // 2
        
        root = BST(l1[mid] )
        root.left = BST.build_BST(self.left, l1[:mid] )
        root.right = BST.build_BST(self.right, l1[mid+1:] )
        return root
    
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
    
    def preorder_iter(self):
        stack = []
        visited = []
        res = []
        stack.append(self)
        
        while stack:
            cur = stack.pop()
            if cur:
                if cur in visited:
                    visited.append(cur)
                    stack.append(cur.right)
                    stack.append(cur.left)
                    stack.append(cur)
                else:
                    res.append(cur.item)
        return res
    
    
    def inorder(self):
        stack = []
        stack.append(self)
        visited = []
        res = []
        
        while stack:
            cur = stack.pop()
            
            if cur:
                if cur not in visited:
                    visited.append(cur)
                    stack.append(cur.right)
                    stack.append(cur)
                    stack.append(cur.left)
                else:
                    res.append(curr.item)
        return res
    
    
    def lowest_common_ancestor(self, integer1, integer2):
        if self.item < min(integer1, integer2):
            return BST.lowest_common_ancestor(self.right, integer1, integer2)
        
        elif self.item > max(integer1, integer2):
            return BST.lowest_common_ancestor(self.left, integer1, integer2)
        
        return self.item
    
    def kth_num(self, k):
        stack = []
        
        while stack or self.item:
            
            while self:
                stack.append(self)
                self = self.left
                
            cur = stack.pop()
            
            k -= 1
            if k == 0:
                return cur.item
            
            self = self.right
    
    
    
    
            
            
            
        
        


if __name__ == "__main__":
    print('start\n')
    
    b = BST()
    b.insert(50)
    # b.insert(25)
    b.display('')
    if b.left.item == None:
        print('none')
    else:
        print('not none')
        
        
        
        