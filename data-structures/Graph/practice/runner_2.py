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


class EdgeList(object):
    def __init__(self, nodes):
        self.node = nodes
        self.item = []
        self.num_of_nodes = len(self.node)
        
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item.append([index1,index2])
        else:
            index1 = item1
            index2 = item2
            self.item.append([index1,index2])
            
    def display(self):
        print(self.item)
        
    
    def edge_list_to_adj_list(self):
        result = AdjacencyList(self.node )
        for i in range(len(self.item) ):
            print(self.item[i][0], self.item[i][1])
            result.item[self.item[i][0]].append(self.item[i][1])
            # result.item[self.item[i][1]].append(self.item[i][0])   #for undirected graph
        return result
    
    def edge_list_to_adj_matrix(self):
        m = np.zeros((self.num_of_nodes, self.num_of_nodes), dtype=bool)
        for i in range(len(self.item) ):
            m[self.item[i][0]][self.item[i][1]] = True
            # m[self.item[i][1]][self.item[i][0]] = True  # For undirected graph
        return m
    
    
class AdjacencyMatrix(object):
    def __init__(self, nodes):
        self.node = nodes
        self.num_of_nodes = len(self.node)
        self.item = np.zeros((self.num_of_nodes, self.num_of_nodes), dtype=bool)
        
    def insert(self, item1, item2):
        if item1 in self.node and item2 in self.node:
            index1 = self.node.index(item1)
            index2 = self.node.index(item2)
            self.item[index1][index2] = True
            #self.item[index2][index1] = True  #For undirected graph
        else:
            index1 = item1
            index2 = item2
            self.item[index1][index2] = True
            #self.item[index2][index1] = True  #For undirected graph
            
    def display(self):
        print(self.item, '\n')
        
        
    def adj_matrix_to_adj_list(self):
        result = AdjacencyList(self.node)
        for i in range(self.num_of_nodes):
            for j in range(self.num_of_nodes):
                if self.item[i][j] == True:
                    result.item[i].append(j)
        return result
    
    def adj_matrix_to_edge_list(self):
        result = EdgeList(self.node)
        for i in range(self.num_of_nodes):
            for j in range(self.num_of_nodes):
                if self.item[i][j] == True:
                    result.item.append([i,j])
        return result



if __name__ == "__main__":
    print('start program\n')
    n = ["Jack", "Nano", "Kitty", "Walter", "Maverick"]
    
    am = AdjacencyMatrix(n)
    am.display()
    am.insert("Jack", "Kitty")
    am.insert("Jack", "Nano")
    am.insert(3, 4)
    am.display()
    
    el = am.adj_matrix_to_edge_list()
    el.display()
    
    
    