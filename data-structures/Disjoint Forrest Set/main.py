# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:31:36 2021

@author: joaqu
"""
from DisjointForrestSet import DSF

# 12 min old
# 9 mins new

if __name__ == "__main__":
    print('start program\n')
    d = DSF(10)
    d.display()
    d.union_by_size(0, 5)
    d.display()
    d.union_by_size(3, 8)
    d.display()
    d.union_by_size(8,5)
    d.display()
    print(d.num_of_sets() )