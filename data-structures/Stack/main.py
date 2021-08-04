# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:24:00 2021

@author: joaqu
"""
from Stack import Stack

if __name__ == "__main__":
    
    print('start program\n')
    
    # Custom stack
    s = Stack()
    
    s.insert(4)
    s.insert(7)
    s.insert(9)
    s.insert(13)
    s.insert(17)
    s.display()
    s.pop()
    s.display()
    s.insert(33)
    s.display()
    
    
    # use list as stack
    # q = []
    # q.append(3)
    # q.append(7)
    # q.append(11)
    # q.append(9)
    # q.pop()
    # print(q)
    # for i in range(len(q)-1, -1, -1 ):
    #     print(q[i])
    