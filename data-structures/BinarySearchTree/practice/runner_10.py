# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 07:17:28 2021

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
        BST.display(self.left, space + '   ')
        

if __name__ == "__main__":
    print('start\n')
    b = BST()
    b.insert(50)
    b.insert(90)
    b.insert(78)
    b.insert(84)
    b.insert(30)
    b.insert(44)
    b.insert(99)
    b.insert(5)
    b.display('')