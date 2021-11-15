# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:13:43 2021

@author: joaqu
"""

def bfs(self, src):
    visited = []
    res = []
    queue = []
    queue.append(src)
    visited.append(src)
    
    while queue:
        cur = queue.pop(0)
        res.append(cur)
        
        for n in self.item[cur]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                prev[n] = cur

        
        