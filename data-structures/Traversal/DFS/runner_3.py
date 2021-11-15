# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:26:01 2021

@author: joaqu
"""

class dfs(self, src):
    res = visited = stack = []
    stack.append(src)
    visited.append(src)
    
    while stack:
        cur = stack.pop()
        res.append(cur)
        
        for n in self.item[cur]:
            if n not in visited:
                visited.append(n)
                stack.append(n)
                prev[n] = cur


