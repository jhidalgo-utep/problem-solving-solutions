# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:11:25 2021

@author: joaqu
"""

def topological(self):
    res = []
    indegree = self.in_degree()
    queue = []
    
    for i in range(len(indegree) ):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        cur = queue.pop(0)
        res.append(cur)
        
        for i in self.item[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
            
    if len(res) == len(queue):
        return res
    return []
            
        
    
    