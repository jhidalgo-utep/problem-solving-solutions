# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:59:38 2021

@author: joaqu
"""
from numpy import np

class DSF(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype = int) - 1
    
    def find_root(self, index):
        if self.item[index] < 0:
            return index
        return self.find_root(self.item[index] )
    
    def union(self, index1, index2):
        r1 = self.find_root(index1)
        r2 = self.find_root(index2)
        if r1 != r2:
            if self.item[r1] < self.item[r2]:
                self.item[r1] += self.item[r2]
                self.item[r2] = r1
            else:
                self.item[r2] += self.item[r1]
                self.item[r1] = r2
                
    