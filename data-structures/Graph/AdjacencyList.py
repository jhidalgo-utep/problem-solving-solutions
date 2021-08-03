# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:21:56 2021

@author: joaqu
"""
import numpy as np

class AdjacencyList(object):
    def __init__(self, nodes):
        self.node = nodes
        self.item = []
        for i in range(len(self.node) ):
            self.item.append( [] )
            
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item[index1].append(index2)
        else:
            index1 = item1
            index2 = item2
            self.item[index1].append(item2)
            
    def display(self):
        print(self.item)
        
    def display_nodes(self):
        print(self.node)
            
    def in_degree(self):
        if self == None:
            return
        result = np.zeros(len(self.item), dtype=int)
        for bucket in range(len(self.item) ):
            for out_degree in range(len(self.item[bucket]) ):
                result[self.item[bucket][out_degree] ] += 1
        return result
    
    
    def adj_list_to_edge_list(self):
        e = []
        for bucket in range(len(self.item) ):
            for edge in range( len(self.item[bucket]) ):
                e.insert( bucket, self.item[bucket][edge] )
        return e
    
    
    def adj_list_to_adj_matrix(self):
        result = np.zeros((len(self.node), len(self.node)), dtype = bool)
        for bucket in range(len(self.item) ):
            for edge in range( len(self.item[bucket]) ):
                result[bucket][self.item[bucket][edge]] = True
        return result
            