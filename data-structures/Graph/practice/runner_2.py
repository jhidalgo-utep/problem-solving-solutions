# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:35:35 2021

@author: joaqu
"""
import numpy as np


class DisjointForrestSet(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype=np.int) - 1
    
    def display(self):
        print(self.item)
        
     #Find with path
    def find_root(self, index):
        if self.item[index] < 0:
            return index
        return self.find_root( self.item[index] )

    #Union by Size
    def union(self, i, j):
        ri = self.find_root(i)
        rj = self.find_root(j)
        #checks if in same subset
        if ri != rj:
            #Checks which dsf is smalller
            
            if self.item[ri] > self.item[rj]:
                self.item[rj] += self.item[ri]  #sum up both and store in least [rj]
                self.item[ri] = rj #tell the greater one [ri] where the least  [ri] one is
            else:
                self.item[ri] += self.item[rj]
                self.item[rj] = ri            
                
    def check_same_set(self, i, j):
        root1 = self.find_root(i)
        root2 = self.find_root(j)
        if root1 != root2:
            return False
        return True

#####################################################
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

    
    #take in an adjceny list, starting point and visit complete
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
    
    
    #take in an adjceny list, starting point and visit complete
    def dfs(self, source, visit_complete):
        stack = [] #initilize stack
        visit_complete.append(source)
        stack.append(source)
        
        while(len(stack) != 0 ):
            current = stack.pop()
            print(current)
            
            for neighbour in self.item[current]:
                if neighbour not in visit_complete:
                    visit_complete.append(neighbour)
                    stack.append(neighbour)
                    #Here you can: prev[neighbour] = current : to state where you came from

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
        
                    
##################################
##################################
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
            
    def insert_list(self, new_list):
        for i in new_list:
            self.item.append([i[0], i[1], i[2]])
        
        
            
            
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
    
    
    # edge_list = self.item[edge1,edge1,weight]
    def kruskal(self):
        self.item = sorted(self.item, key=lambda a: a[2])
        ds = DisjointForrestSet(len(self.item))
        min_span_tree = []
        for edge in self.item:
            if ds.check_same_set(edge[0], edge[1]) == False:
                min_span_tree.append(edge)
                ds.union(edge[0], edge[1])
        return min_span_tree
        
    

##################################
##################################
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
    
    
    
    
    