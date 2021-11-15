# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:16:42 2021

@author: joaqu
"""

def dfs(self):
    res = []
    visited = []
    stack = []
    stack.append(self)
    visited.append(self)
    
    while stack:
        cur = stack.pop()
        res.append(cur)
        
        for i in self.item[cur]:
            if i not in visited:
                visited.append(i)
                stack.append(i)
                
    return res
    
    
    
    