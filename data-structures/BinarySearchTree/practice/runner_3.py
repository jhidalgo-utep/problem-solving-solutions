# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:31:31 2021

@author: joaqu
"""
# 58 min

class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
        
    def get_item(self):
        return self.item

    def insert(self, new_item):
        if self.get_item() == None:
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
        BST.display(self.right, space + "   ")
        print(space, self.get_item() )
        BST.display(self.left, space + "   ")
        
    def sum_of_nodes(self):
        if self == None or self.get_item() == None:
            return 0
        return self.get_item() + BST.sum_of_nodes(self.left) + BST.sum_of_nodes(self.right)
    
    def num_of_nodes(self):
        if self == None or self.get_item() == None:
            return 0
        return 1 + BST.num_of_nodes(self.left) + BST.num_of_nodes(self.right)
    
    def sum_at_depth(self, depth):
        if self == None or self.get_item() == None:
            return 0
        if depth == 0:
            return self.get_item()
        return BST.sum_at_depth(self.left, depth - 1) + BST.sum_at_depth(self.right, depth - 1)
    
    def find_depth_of_item(self, key_item):
        if self == None or self.get_item() == None:
            return -1
        if self.get_item() == key_item:
            return 0
        
        if self.get_item() < key_item:
            d = BST.find_depth_of_item(self.right, key_item)
        else:
            d = BST.find_depth_of_item(self.left, key_item)
        if d < 0:
            return -1
        return d + 1
    
    def smallest(self):
        if self == None or self.get_item() == None:
            return 
        if self.left == None:
            return self.get_item()
        return BST.smallest(self.left)
    
    def largest(self):
        if self == None or self.get_item() == None:
            return 
        if self.right == None:
            return self.get_item()
        return BST.largest(self.right)
    
    def find(self, key_item):
        if self == None or self.get_item() == None:
            return False
        
        if self.get_item() == key_item:
            return True
        
        if self.get_item() < key_item:
            return BST.find(self.right, key_item)
        else:
            return BST.find(self.left, key_item)
    
    def print_at_depth(self, depth):
        if self == None or self.get_item() == None:
            return
        if depth == 0:
            print(self.get_item(), end = ' ')
        BST.print_at_depth(self.left, depth - 1)
        BST.print_at_depth(self.right, depth - 1)
        
    
    def extract_to_list(self, my_list):
        if self == None or self.get_item() == None:
            return
        BST.extract_to_list( self.left, my_list )
        my_list.append( self.get_item() )
        BST.extract_to_list( self.right, my_list )
        
    
    def build_BST(self, my_list):
        if len(my_list) == 0:
            return
        
        mid = len(my_list) // 2
        
        self = BST(my_list[mid] )
        self.left = BST.build_BST(self.left, my_list[:mid] )
        self.right = BST.build_BST(self.right, my_list[mid+1:] )
        return self
    
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
    
    def lowest_common_anncestor(self, integer1, integer2):
        if self == None or self.get_item() == None:
            return
        
        if self.get_item() < min(integer1, integer2):
            return BST.lowest_common_anncestor(self.right, integer1, integer2)
        elif self.get_item() > max(integer1, integer2):
            return BST.lowest_common_anncestor(self.left, integer1, integer2)
        
        return self.get_item()
    
    def kth_num(self, k):
        stack = []
        stack.append(self)
        while stack or self.get_item():
            while self:
                stack.append(self)
                self = self.left
            
            self = stack.pop()
            k -= 1
            if k == 0:
                return self.get_item()
            
            self = self.right
        return 
        
    
    def preorder_iter(self):
        stack = []
        result = []
        visited = []
        stack.append(self )
        
        while stack:
            curr = stack.pop()
            if curr:
                if curr in visited:
                    result.append(curr.get_item() )
                else:
                    visited.append(curr)
                    stack.append(curr.right)
                    stack.append(curr.left)
                    stack.append(curr)
        return result
    
    
    def inorder_iter(self):
        stack = []
        result = []
        visited = []
        stack.append(self)
        while stack:                
            curr = stack.pop()
            if curr:
                if curr in visited:
                    result.append(curr.get_item() )
                else:
                    visited.append( curr )
                    stack.append(curr.right)
                    stack.append(curr)
                    stack.append(curr.left)
        return result
        
    def postorder_iter(self):
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
                    stack.append(curr)
                    stack.append(curr.right)
                    stack.append(curr.left)
        return result
    
        

if __name__ == "__main__":
    print('start\n')
    b = BST()
    b.insert(30)
    b.insert(20)
    b.insert(40)
    b.insert(45)
    b.insert(18)
    b.insert(37)
    b.insert(200)
    b.display(' ')
    print()
    print('sum at depth 2: ', b.sum_at_depth(2) )
    print('num of nodes: ', b.num_of_nodes() )
    print('sum of nodes: ',  b.sum_of_nodes() )
    print( 'find depth of 37: ', b.find_depth_of_item(37) )
    print('smallest', b.smallest() )
    print('largest',  b.largest() )
    print( 'find 45: ', b.find(45) )
    
    print( 'print at depth 2: ', end = '')
    print( b.print_at_depth(2))
    
    temp_list = []
    BST.extract_to_list(b, temp_list) 
    print(temp_list)
    
    b2 = BST.build_BST(None, temp_list)
    # b2.display(' ')
    
    print(b.height() )
    
    print( 'LCA: ', b.lowest_common_anncestor(45, 200) )
    
    print('3 kth item: ', b.kth_num(100) )
    
    
    
    
    
    
    
    pre = b.preorder_iter()
    print(pre)
    
    inorder = b.inorder_iter()
    print(inorder)
    
    post = b.postorder_iter()
    print(post)
    
    
    
    
    