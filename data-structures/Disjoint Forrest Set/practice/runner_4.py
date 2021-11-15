# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:38:19 2021

@author: joaqu
"""
import numpy as np


class DSF(object):
    def __init__(self, size):
        self.item = np.zeros(size, dtype=int)
        
    def root(self, index1):
        if self.item[index1] < 0:
            return index1
        return self.root(self.item[index1] )
        
    
    def union(self, index1, index2):
        r1 = self.root(index1)
        r2 = self.root(idnex2)
        if r1 != r2:
            if self.item[r1] < self.item[r2]:
                self.item[r1] += self.item[r2]
                self.item[r2] = r1
            else:
                self.item[r2] += self.item[r1]
                self.item[r1] = r2
        
    def check_same_set(self, index1, index2):
        r1 = self.root(index1)
        r2 = self.root(index2)
        
        return r1 == r2
    
    def display(self):
        print(self.item)
        
    def num_of_sets(self):
        counter = 0
        for i in self.item:
            if i < 0:
                counter += 1
        return counter
    
        
        




