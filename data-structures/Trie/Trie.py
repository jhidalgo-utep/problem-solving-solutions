# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:36:59 2021

@author: joaqu
"""
from Node import Node

# ### Practice !!! ###
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
    
    def search(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
            
        if iter_node.is_leaf:
            return True
        return False
    
    def search_prefix(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
            
        return True
    