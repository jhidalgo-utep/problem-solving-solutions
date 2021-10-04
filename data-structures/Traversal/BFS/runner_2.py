# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:27:13 2021

@author: joaqu
"""
import numpy as np

def bfs(self, source, visited):
    queue = []
    prev = np.zeros(len(self.item), dtype = int )
    queue.append(source)
    visited.append(source)
    
    while queue:
        curr = queue.pop(0)
        print(curr)
        
        for neighbor in self.item[curr]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                prev[neighbor] = curr