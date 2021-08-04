# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:44:47 2021

@author: joaqu
"""
from Queue import Queue

if __name__ == "__main__":
    print('start program\n')
    q = Queue()
    q.insert(2)
    q.insert(5)
    q.insert(8)
    q.insert(13)
    q.display()
    print(q.pop() )
    q.pop()
    q.display()
    q.insert(24)
    q.display()
    print(q.peak())
    
