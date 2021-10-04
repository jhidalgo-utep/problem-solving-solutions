# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:21:53 2021

@author: joaqu
"""

class Node(object):
    def __init__(self):
        self.children = {}
        self.is_leaf= False
    

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
            if c in iter_node.children:
                iter_node = iter_node.children[c]
            else:
                return False
            
        return True
    
    def search(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
        return iter_node.is_leaf
    

if __name__ == "__main__":
    t = Trie()
    t.insert('soccer')
    t.insert('socks')
    t.insert('red')
    
    print( t.search('soccer'))
    print( t.prefix('soccer') )
    