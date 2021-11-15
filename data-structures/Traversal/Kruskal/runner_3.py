# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:32:40 2021

@author: joaqu
"""

def kruskal(self):
    res = []
    self.item = sorted(self.item, key = lambda x:x[2] )
    d = DFS()
    for e in self.item:
        if not d.check_same_set(e[0], e[1]):
            d.union(e[0], e[1])
            res.append(e)
            
    return res          

    
            





