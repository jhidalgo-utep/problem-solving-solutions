# -*- coding: utf-8 -*-

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
        
        BST.display(self.right, space+'  ')
        print(space, self.item)
        BST.display(self.left, space+'  ')
        

if __name__ == "__main__":
    print('start program')
    b = BST()
    b= b.insert(22)
    b= b.insert(7)
    b= b.insert(59)
    b.display('')
    
    