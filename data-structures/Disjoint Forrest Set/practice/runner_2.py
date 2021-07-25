# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:32:13 2021

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
            return False, i, j
        return True, i, j
    
    def num_of_sets(self):
        c = 0
        for i in range(len(self.item) ):
            if self.item[i] < 0:
                c += 1
        return c
   
    
    #Regular union
    # def union_regular(self, i, j):
    #     ri = self.find_root(i)
    #     rj = self.find_root(j)
    #     if ri != rj:
    #         self.item[rj] = ri
    

if __name__ == "__main__":
    d = DisjointForrestSet(5)
    d.display()
    d.union(0, 3)
    d.display()