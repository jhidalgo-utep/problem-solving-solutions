# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:30:54 2021

@author: joaqu
"""

def kruskal(self):
    self.item = sorted(self.item, key = lambda x:x[2])
    res = []
    d = DFS(len(self.item) )
    
    for e in self.item:
        if not d.check_same_set(e[0], e[1] ):
            d.union(e[0], e[1] )
            res.append(e)
    

    return res
            
            