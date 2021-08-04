# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:01:09 2021

@author: joaqu
"""
from Set import Set

if __name__ == "__main__":
    
    print('start program \n')
    
    ### Custom Set class
    s = Set()
    
    s.insert("dog")
    s.insert('cat')
    s.display()
    s.pop('dog')
    s.display()
    s.insert('fish')
    s.insert('elephant')
    s.display()
    s.pop('fish')
    s.display()
    ##########################
    
    # # set python library
    # s = set()
    # s.add('john')
    # s.add('nano')
    # s.remove('john')
    
    # d = set()
    # d.add('kitty')
    
    # m = s.union(d)
    # print(m)
    
    