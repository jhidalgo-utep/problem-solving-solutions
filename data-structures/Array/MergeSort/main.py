# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:28:27 2021

@author: joaqu
"""

#  ### Practice !!! ###
def MergeSort(my_list):
    if len(my_list) <= 1:
        return 
    
    mid_index = len(my_list) // 2
    
    left_sub_list = my_list[:mid_index]
    right_sub_list = my_list[mid_index:]
    
    MergeSort(left_sub_list)
    MergeSort(right_sub_list)
    
    left_pointer_iterator = right_pointer_iterator = result_iterator = 0
    
    while left_pointer_iterator < len(left_sub_list) and right_pointer_iterator < len(right_sub_list):
        if left_sub_list[left_pointer_iterator] < right_sub_list[right_pointer_iterator]:
            my_list[result_iterator] = left_sub_list[left_pointer_iterator]
            left_pointer_iterator += 1
            result_iterator += 1
        else:
            my_list[result_iterator] = right_sub_list[right_pointer_iterator]
            right_pointer_iterator += 1
            result_iterator += 1
    
    while left_pointer_iterator < len(left_sub_list):
        my_list[result_iterator] = left_sub_list[left_pointer_iterator]
        left_pointer_iterator += 1
        result_iterator += 1
    
    while right_pointer_iterator < len(right_sub_list):
        my_list[result_iterator] = right_sub_list[right_pointer_iterator]
        right_pointer_iterator += 1
        result_iterator += 1



if __name__ == "__main__":
    print('start program\n')
    
    test = [45,23,2,90,37,95,45,50,91,26,21]
    
    MergeSort(test)
    
    print(test)
    
    
    
    
    