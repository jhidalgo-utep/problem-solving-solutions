# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:54:43 2021

@author: joaqu
"""

def topologial(self):
    res = []
    queue = []
    indegree = self.in_degree()
    
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
            
    if len(res) == len(self.item):
        return True
    return False
                
                




