# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:35:35 2021

@author: joaqu
"""
import numpy as np


class AdjacencyList(object):
    def __init__(self, nodes):
        self.node = nodes
        self.num_of_nodes = len(self.node)
        self.item = []
        for i in range(self.num_of_nodes):
            self.item.append([])
    
    def in_degree(self):
        result = []
        for vertice in range(len(self.item) ):
            result.append(0)
        
        for i in range(len(self.item) ):
            for j in range(len(self.item[i]) ):
                result[ self.item[i][j] ] += 1
        return result
        
            
    def display(self):
        print(self.item)
        
    def display_nodes(self):
        print(self.node)
        
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item[index1].append(index2)
        else:
            index1 = item1
            index2 = item2
            self.item[index1].append(index2)
            
    def adj_list_to_edge_list(self):
        result = []
        for i in range(self.num_of_nodes):
            for j in range(len(self.item[i]) ):
                result.append([i,self.item[i][j]] )
        return result
    
    def adj_list_to_adj_matrix(self):
        result = np.zeros((self.num_of_nodes, self.num_of_nodes), dtype=bool)
        for i in range(self.num_of_nodes):
            for j in range(len(self.item[i]) ):
                result[i, self.item[i][j] ] = True
                result[self.item[i][j], i ] = True
        return result
        
    
    # ### Practice!!! ###
    def topological(self):
        result = []
        queue = []
        indegree = self.in_degree()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while len(queue) > 0:
            vertex = queue.pop(0)
            result.append(vertex)
            for u in self.item[vertex]:
                indegree[u] = indegree[u] - 1
                if indegree[u] == 0:
                    queue.append(u)
        
        if len(result) == len(self.item):
            return result
        else:
            return []                
                


if __name__ == "__main__":
    print('start program\n')

    n = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    a = AdjacencyList(n)
    
    a.insert("I", "L")
    a.insert("F", "K")
    a.insert("E", "D")
    a.insert("C", "A")
    a.insert("H", "J")
    a.insert("D", "G")
    a.insert("E", "A")
    a.insert("F", "J")
    a.insert("D", "H")
    a.insert("J", "L")
    a.insert("A", "D")
    a.insert("E", "F")
    a.insert("H", "I")
    a.insert("K", "J")
    a.insert("G", "I")
    a.insert("B", "D")
    a.insert("J", "M")
    a.insert("C", "B")
    res = a.topological()
    print(res)
    
    
    
    
    