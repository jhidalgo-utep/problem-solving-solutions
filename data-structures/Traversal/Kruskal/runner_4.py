# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:08:57 2021

@author: joaqu
"""

def kruskal(self):
    res = []
    self.item = sorted(self.item, key = lambda x:x[2] )
    d = DFS(len(self.item) )
    
    for e in self.item:
        if not d.check_same_set(e[0], e[1] ):
            d.union(e[0], e[1] )
            res.append(e)
            
    return res
    
    
    
    