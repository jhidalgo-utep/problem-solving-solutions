# -*- coding: utf-8 -*-
import math

class BST(object):
    def __init__(self, item = None):
        self.left = None
        self.right = None
        self.item = item
    
    
    def insert(self, new_item):
        if self == None or self.item == None:
            self = BST(new_item)
        elif self.item > new_item:
            self.left = BST.insert(self.left, new_item)  
        elif self.item < new_item:
            self.right = BST.insert(self.right, new_item)
        return self
            
    
    def display(self, space):
        if self == None or self.item == None:
            return
        BST.display(self.right, space+'   ')
        print(space, self.item)
        BST.display(self.left, space+'   ')
        
    def smallest(self):
        if self.item == None:
            return 
        elif self.left == None:
            return self.item
        return BST.smallest(self.left)
    
    def largest(self):
        if self.item == None:
            return
        elif self.right == None:
            return self.item
        return BST.largest(self.right)
    
    def find(self, key_item):
        if self == None or self.item == None:
            return False
        elif self.item == key_item:
            return True
        elif self.item > key_item:
            return BST.find(self.left, key_item)
        else:
            return BST.find(self.right, key_item)
        
    def print_at_depth(self, key_depth):
        if self == None:
            return
        elif key_depth == 0:
            print(self.item)
            return
        else:
            BST.print_at_depth(self.left, key_depth-1)
            BST.print_at_depth(self.right, key_depth-1)
            
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
        if self == None:
            return
        BST.extract_to_list(self.left, new_list)
        new_list.append(self.item)
        BST.extract_to_list(self.right, new_list)
        
    def build_BST(self, L):
        if L is None or len(L) == 0:
            return
        mid = len(L)//2
        
        root = BST(L[mid])
        
        root.left =  BST.build_BST( self, L[:mid] )
        root.right =  BST.build_BST( self, L[mid+1:] )
        
        return root
        
    def number_of_nodes(self):
        if self == None:
            return 0
        return 1 + BST.number_of_nodes(self.left) + BST.number_of_nodes(self.right) 
    
    def sum_of_tree(self):
        if self == None or self.item == None:
            return 0
        return self.item + BST.sum_of_tree(self.left) + BST.sum_of_tree(self.right)
        
    def height(self):
        if self == None:
            return 0
        left = BST.height(self.left)
        right = BST.height(self.right)
        
        if self.left == None and self.right == None:
            return max(left,right)
        
        if left>right:
            return left +1
        return right +1
            
        
    def sum_at_depth(self, key_depth):
        if self == None:
            return 0
        elif key_depth == 0:
            return self.item
        if self.left == None and self.right == None:
            return 0
        return BST.sum_at_depth(self.left, key_depth-1) + BST.sum_at_depth(self.right, key_depth-1)
        
        
if __name__ == "__main__":
    print('start program')
    S = [10,20,30,40,50]
    Q = BST.build_BST(None, S)
    Q.display('')
    print('\n\n')
    
    b = BST()
    b = b.insert(22)
    b = b.insert(7)
    b = b.insert(59)
    b = b.insert(13)
    b = b.insert(3)
    b = b.insert(99)
    b = b.insert(16)
    b = b.insert(49)
    b.display('')
    
    print('smallest: ' , b.smallest() )
    print('largest: ', b.largest() )
    searchForInt = 17
    print('find', searchForInt, ':', b.find(searchForInt) )
    BST.print_at_depth(b, 0) 
    
    print('find depth: ', BST.find_depth_of_item(b, 16) )
    
    print('num of nodes: ', BST.number_of_nodes(b) )
    
    print('sum nodes: ', BST.sum_of_tree(b) )
    
    print('height: ', BST.height(b) )
    
    desired_depth = 3
    print('sum at depth', desired_depth, ':', BST.sum_at_depth(b, desired_depth) )
    
    
    
    

    
    