# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:43:21 2021

@author: joaquin
"""

from LinkedList import LinkedList

# Use 'x = LinkedList()' to create a Linked List to manipulate. 
# Then be able to use methods from LinkedList.py class like: 'x.isEmpty()'.


#Main Method
if __name__ == "__main__":

    print("Begin main program...\n")
    
    LL = LinkedList() #init data struc
    
    print( LL.isEmpty() ) 

    LL.insert(55) 
    LL.insert(33)
    
    print( LL.isEmpty() )
    
    LL.printList() 

    print(LL.get_head_data() )