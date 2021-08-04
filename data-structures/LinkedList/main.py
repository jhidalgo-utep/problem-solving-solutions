# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:43:21 2021

@author: joaquin
"""

from LinkedList import LinkedList

if __name__ == "__main__":
    print('start program\n')
    
    ll = LinkedList()
    
    ll.insert(21)
    ll.insert(5)
    ll.insert(44)
    ll.insert(37)
    ll.insert(82)
    
    ll.display()
    
    ll.delete(82)
    ll.insert(88)
    
    ll.display()
    
    print('list length: ', ll.get_list_length())
    
    ll.reverse_list()
    ll.display()
    ll.insert(99)
    ll.insert(2)
    ll.display()
    ll.insert(77)
    ll.display()
    
    