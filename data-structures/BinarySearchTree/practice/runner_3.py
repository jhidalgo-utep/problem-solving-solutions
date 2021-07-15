# -*- coding: utf-8 -*-

import math
class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
    
    def insert(self, new_item):
        if self == None or self.item == None:
            self = BST(new_item)
        elif self.item > new_item:
            self.left = BST.insert(self.left, new_item)
        elif self.item < new_item:
            self.right = BST.insert(self.right, new_item)
        return self
    
    def display(self, space):
        if self == None:
            return
        BST.display(self.right, space + '  ')
        print(space, self.item)
        BST.display(self.left, space + '  ')
    
    def smallest(self):
        if self == None:
            return
        elif self.left == None:
            return self.item
        return BST.smallest(self.left)
    
    def find(self, key_item):
        if self == None or self.item == None:
            return False
        elif self.item == key_item:
            return True
        elif self.item > key_item:
            return BST.find(self.left, key_item)
        return BST.find(self.right, key_item)
    
    def print_at_depth(self, depth):
        if self == None or self.item == None:
            return
        elif depth == 0:
            print(self.item)
        BST.print_at_depth(self.left, depth -1)
        BST.print_at_depth(self.right, depth -1)
        
    def find_depth_of_item(self, key_item):
        if self == None or self.item == None:
            return -1
        elif self.item == key_item:
            return 0
        if self.item > key_item:
            d = BST.find_depth_of_item(self.left, key_item)
        else:
            d = BST.find_depth_of_item(self.right, key_item)
        if d < 0:
            return -1
        return d+1
    
    
    def extract_to_list(self, new_list):
        if self == None or self.item == None:
            return
        BST.extract_to_list(self.left, new_list)
        new_list.append(self.item)
        BST.extract_to_list(self.right, new_list)
        
        
    def build_bst(self, list_of_nums):
        if list_of_nums == None or len(list_of_nums) == 0:
            return
        
        mid = len(list_of_nums)//2
        
        root = BST(list_of_nums[ mid ])
        
        root.left = BST.build_bst(self, list_of_nums[ :mid ])
        root.right = BST.build_bst(self, list_of_nums[ mid+1: ])
        
        return root
    
    def number_of_nodes(self):
        if self == None or self.item == None:
            return 0
        return 1 + BST.number_of_nodes(self.left) + BST.number_of_nodes(self.right)
    
    def sum_of_nodes(self):
        if self == None or self.item == None:
            return 0
        return self.item + BST.number_of_nodes(self.left) + BST.number_of_nodes(self.right)
    
    def height(self):
        if self == None or self.item == None:
            return 0

        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left, right)
        
        if left > right:
            return left+1
        return right + 1
    
    def sum_at_depth(self, key_depth):
        if self == None or self.item == None:
            return 0
        elif key_depth == 0:
            return self.item
        if self.left == None and self.right == None:
            return 0
        return BST.sum_at_depth(self.left, key_depth - 1) + BST.sum_at_depth(self.right, key_depth - 1)
        

if __name__ == "__main__":
    print('hello')
    
    b = BST()
    b = b.insert(21)
    b = b.insert(1)
    b = b.insert(30)
    b = b.insert(19)
    b = b.insert(37)
    b = b.insert(4) 
    
    b.display('')
    
    # print( b.smallest() )
    # print( b.find(4) )
    
    # b.print_at_depth(1)
    
    # print( b.find_depth_of_item(4) )
    l = []
    b.extract_to_list(l)
    print(l)
    
    c = BST.build_bst(None, l)
    c.display('')
    
    print(c.number_of_nodes() )
    
    print(c.height() )
    
    print( c.sum_at_depth(4) )
    
    
    
    
    
    