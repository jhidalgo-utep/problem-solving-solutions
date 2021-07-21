# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:39:54 2021

@author: joaqu
"""


if __name__ == "__main__":
    print('start program\n')
    s1 = set()
    s1.add(1)
    s1.add(55)
    s1.add(37)
    s1.add(2)
    
    if 3 in s1:
        s1.remove(3)
    if 1 in s1:
        s1.remove(1)
    print(s1)
    
    
    s2 = set( [1,2,3,4,5,6,7,8,9] )
    s2.add(1)
    print(s2)
    
     # s1 | s2
    print( s1.union(s2) )
    
    print(s1 == s2)
   
    # s1 & s2
    print( s1.intersection(s2) )
    
    s4 = set([1,2,3,4,5])
    s5 = set([2,4])
    
    #print true if s4 is a subset of s5
    print(s4 <= s5)
    #print true if s4 is a superset of s5
    print(s4 >= s5)