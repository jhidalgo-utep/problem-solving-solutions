# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:03:58 2021

@author: joaqu
"""

def bfs(self):
    visited = []
    queue = []
    res = []
    queue.append(self)
    visited.append(self)
    
    while queue:
        cur = queue.pop()
        res.append(cur)
        
        for n in self.item[cur]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                
    return res