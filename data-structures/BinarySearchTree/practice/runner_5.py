# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:13:44 2021

@author: joaqu
"""

#this BST is actually BST_Nodes that make up a BST
class BST(object):
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None
    
    #self is the data structure BST
    def insert(self, new_item):
        if self == None or self.item == None:
            self.item = new_item
        else:
            if new_item < self.item:
                if self.left == None:
                    self.left = BST(new_item)
                else:
                    self.left.insert(new_item)
            else:
                if self.right == None:
                    self.right = BST(new_item)
                else:
                    self.right.insert(new_item)
                    
    def display(self, space):
        if self == None or self.item == None:
            return
        BST.display(self.right, space + '   ')
        print(space, self.item)
        BST.display(self.left, space + '   ')
        
    def smallest(self):
        if self == None or self.item == None:
            return
        if self.left == None:
            return self.item
        return BST.smallest(self.left)
    
    def largest(self):
        if self == None or self.item == None:
            return
        if self.right == None:
            return self.item
        return BST.largest(self.right)
    
    def find(self, key_item):
        if self == None or self.item == None:
            return False
        elif self.item == key_item:
            return True
        elif self.item < key_item:
            return BST.find(self.right, key_item)
        return BST.find(self.left, key_item)
    
    def print_at_depth(self, key_depth):
        if self == None or self.item == None:
            return 
        elif key_depth == 0:
            print(self.item)
        BST.print_at_depth(self.left, key_depth - 1)
        BST.print_at_depth(self.right, key_depth - 1)
        
    def find_depth_of_item(self, key_item):
        if self == None or self.item == None:
            return -1
        elif self.item == key_item:
            return 0
        else:
            if self.item > key_item:
                d = BST.find_depth_of_item(self.left, key_item)
            else:
                d = BST.find_depth_of_item(self.right, key_item)
            if d < 0:
                return -1
            return d+1
        
    def extract_to_list(self, L):
        if self == None or self.item == None:
            return
        BST.extract_to_list(self.left, L)
        L.append(self.item)
        BST.extract_to_list(self.right, L)
    
    def build_BST(self, list_of_items):
        if list_of_items == None or len(list_of_items) == 0:
            return
        mid = len(list_of_items) // 2
        self = BST( list_of_items[mid] )
        self.left = BST.build_BST(self.left, list_of_items[:mid] )
        self.right = BST.build_BST(self.right, list_of_items[mid+1:] )
        return self
    
    def number_of_nodes(self):
        if self == None or self.item == None:
            return 0
        return 1 + BST.number_of_nodes(self.left) + BST.number_of_nodes(self.right)
    
    def sum_nodes(self):
        if self == None or self.item == None:
            return 0
        return self.item + BST.sum_nodes(self.left) + BST.sum_nodes(self.right)
    
    def height(self):
        if self == None or self.item == None:
            return 0
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left,right)
        if left > right:
            return left +1
        return right +1
    
    def sum_at_depth(self, depth):
        if self == None or self.item == None:
            return 0
        elif depth == 0:
            return self.item
        # if self.left == None and self.right == None:
        #     return 0
        return BST.sum_at_depth(self.left, depth-1) + BST.sum_at_depth(self.right, depth-1)        
        
    
    
if __name__ == "__main__":
    print('start program...\n')
    b = BST()
    #Needs some work because now the BST doesnt need to return anything after inserting
    
    
    # b = b.insert(21)
    # b = b.insert(49)
    
    
    
    