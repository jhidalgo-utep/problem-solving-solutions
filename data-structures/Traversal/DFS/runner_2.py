# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:30:56 2021

@author: joaqu
"""
# 2 mins

def dfs(self, source, visited):
    stack = []
    prev = np.zeros(len(self.item), dtype = int)
    stack.append(source)
    visited.append(source)
    
    while stack:
        curr = stack.pop()
        print(curr)
        
        for neighbor in self.item[curr]:
            if neighbor not in visied:
                visited.append(neighbor)
                stack.append(neighbor)
                prev[neighbor] = curr
                
                
                
            