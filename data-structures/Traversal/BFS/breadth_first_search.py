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
    
    
    # #take in an adjceny list, starting point and visit complete
    def bfs(self, source, visit_complete):
        queue = [] # iniztilze queue
        visit_complete.append(source)
        queue.append(source)
        
        while(len(queue) != 0 ):
            current = queue.pop(0)
            print(current)
            
            for neighbour in self.item[current]:
                if neighbour not in visit_complete:
                    visit_complete.append(neighbour)
                    queue.append(neighbour)
                    #Here you can: prev[neighbour] = current : to state where you came from
                    
                    
                    
if __name__ == "__main__":
    print('start program\n')
    n = ["Jack", "Nano", "Kitty", "Food", "Water", "Grass", "Treat", "Bread", "Healthy", "Obesse"]
    
    a = AdjacencyList(n)
    a.insert("Jack", "Nano")
    a.insert("Jack", "Kitty")
    a.insert("Nano", "Food")
    a.insert("Nano", "Grass")
    a.insert("Nano", "Treat")
    a.insert("Kitty", "Water")
    a.insert("Food", "Obesse")
    a.insert("Treat", "Bread")
    a.insert("Water", "Healthy")
    a.display_nodes()
    a.display()
    print()
    print()
    a.bfs(0, [] )