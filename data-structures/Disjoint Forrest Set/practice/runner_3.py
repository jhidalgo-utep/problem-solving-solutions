# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:27:24 2021

@author: joaqu
"""
import numpy as np

class DisjointForrestSet(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype = int)-1
    
    
    def display(self):
        print(self.item, '\n')
        
    
    def find_root(self, index):
        if self.item[index]<0:
            return index
        return self.find_root(self.item[index] )
    
    
    def union(self, index1, index2):
        r1 = self.find_root(index1)
        r2 = self.find_root(index2)
        if r1 != r2:
            if self.item[r1] > self.item[r2]:
                self.item[r2] += self.item[r1]
                self.item[r1] = r2
            else:
                self.item[r1] += self.item[r2]
                self.item[r2] = r1
                
    def num_of_sets(self):
        c = 0
        for i in range(len(self.item) ):
            if self.item[i] < 0:
                c += 1
        return c
                
    
        
if __name__ == "__main__":
    print('start program\n')
    d = DisjointForrestSet(5)
    d.display()
    d.union(0, 3)
    d.display()
    d.union(2, 0)
    d.display()
    d.union(1, 4)
    d.display()
    print(d.num_of_sets() )