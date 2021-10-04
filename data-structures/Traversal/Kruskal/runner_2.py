# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:34:19 2021

@author: joaqu
"""

def kruskal(self):
    min_span = []
    self.item = sorted(self.item, key = lambda a:a[2])
    d = DSF(len(self.item) )
    for e in self.item:
        if d.check_same_set(e[0], e[1] ) == False:
            d.union(e[0]. e[1] )
            min_span.append(e)
    return min_span