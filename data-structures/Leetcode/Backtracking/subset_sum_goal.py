# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:38:38 2021

@author: joaqu
"""

#Set of int, last index, goal
def get_goal_subset(given_set, last, goal):
    if goal == 0:
        return True, []
    if goal < 0 or last < 0:
        return False, []
    
    res, returned_subset = get_goal_subset( given_set, last-1, goal - given_set[last] )
    if res:
        returned_subset.append(given_set[last])
        return True, returned_subset
    else:
        return get_goal_subset(given_set, last-1, goal)
        

if __name__ == "__main__":
    print('start program')
    
    sack = [2,3,5,6,9]
    print( get_goal_subset(sack, 4, 11) )