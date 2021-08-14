# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:34:25 2021

@author: joaqu
"""

# ### PRACTICE (small adjustment) ###

def merge_sort(L):
    if len(L) <= 1:
        return 
    
    mid = len(L) // 2
    
    left_sub = L[:mid]
    right_sub = L[mid:]
    
    merge_sort( left_sub )
    merge_sort( right_sub )
    
    lp = rp = list_pointer = 0
    
    while lp < len(left_sub) and rp < len(right_sub):
        if left_sub[lp] < right_sub[rp]:
            L[list_pointer] = left_sub[lp]
            lp += 1
        else:
            L[list_pointer] = right_sub[rp]
            rp += 1
        list_pointer += 1
    
    while lp < len(left_sub):
        L[list_pointer] = left_sub[lp]
        lp += 1
        list_pointer += 1
    
    while rp < len(right_sub):
        L[list_pointer] = right_sub[rp]
        rp += 1
        list_pointer += 1
    
        
        

if __name__ == "__main__":
    print('start program\n')
    n = [45, 10, 2, 9, 93, 23, 60, 40, 20]
    merge_sort(n)
    print(n)
    