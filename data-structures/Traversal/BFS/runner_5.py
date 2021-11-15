# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:18:43 2021

@author: joaqu
"""

class dfs(self, src, visited):
    stack = []
    stack.append(src)
    visited.append(src)
    res = []
    
    while stack:
        cur = stack.pop()
        res.append(cur)
        
        for n in self.item[cur]:
            if n not in visited:
                visited.append(n)
                stack.append(n)
        