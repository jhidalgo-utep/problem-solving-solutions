# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:44:47 2021

@author: joaqu
"""
from Queue import Queue

#14 mins old
# 10 mins new

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
    
    
    print('\n')
    q2 = []
    q2.append(35)
    q2.append(88)
    q2.append(20)
    q2.append(18)
    q2.append(17)
    print(q2)
    q2.pop(0)
    print( q2)
    
    for i in range(len(q2)):
        print(q2[i], end = ' ')
