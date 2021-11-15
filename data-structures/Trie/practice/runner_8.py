# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:40:17 2021

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
    
    def search(self, word):
        iter_node = self.root
        for c in word:
            if c not in iter_node.children:
                return False
            iter_node = iter_node.children[c]
        return iter_node.is_leaf


if __name__ == "__main__":
    print('start\n')
    
    t = Trie()
    
    t.insert('soccer')
    t.insert('socks')
    
    print( t.search('soccer') )
    print( t.prefix('sp'))
                
                
        
        
        
        