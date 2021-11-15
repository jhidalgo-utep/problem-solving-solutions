# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:00:14 2021

@author: joaqu
"""

class Node(object):
    def __init__(self):
        self.children = {}
        self.is_leaf = False

class Trie(object):
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        iter_node = self.root
        
        for c in word:
            if c not in iter_node.children:
                iter_node.children[c] = Node()
            iter_node = iter_node.children[c]
            
        iter_node.is_leaf = True
    
    def prefix(self, word):
        iter_node = self.root
        
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
        return True
    
    
    
            