# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:37:31 2021

@author: joaqu
"""
# 7 mins

def topological_sort(self):
    queue = []
    result = []
    
    indegree = self.get_indegree()
    for i in range( len(indegree) ):
        if 0 == indegree[i]:
            queue.append(i)
            
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        
        for n in self.item[vertex]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append( n )
    
    if len(result) == len(self.item):
        return result
    return []
            