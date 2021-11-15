# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:35:18 2021

@author: joaqu
"""

def merge_sort(nums):
    # 1st we want to split the array in halfs, left and right
    # recursivly call those arrays (left and right) to keep spliting until base case
    # then adjust the array passed in as array
    
    if len(nums) <= 1:
        return
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    lp = rp = ip = 0
    
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            nums[ip] = left[lp]
            lp += 1
        else:
            nums[ip] = right[rp]
            rp += 1
        ip += 1
    
    while lp < len(left):
        nums[ip] = left[lp]
        lp += 1
        ip += 1
    
    while rp < len(left):
        nums[i] = right[rp]
        rp += 1
        i += 1
    

    
    

if __name__ == "__main__":
    print('start\n')
    
    q1 = [100, 40, 88, 20]
    
    print(q1)
    merge_sort(q1)
    print(q1)
    
    
    