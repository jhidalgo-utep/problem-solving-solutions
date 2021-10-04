# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:27:25 2021

@author: joaqu
"""

# Q1: single number
# input: array of integers with all nums having a duplicate except 1
# output: the single number in array that has no duplicates

# PRACTICE !!
# Q2: remove duplicates:
# input: array of int's Sorted w/ or w/o duplicates
# output: int of length of array w/o duplicates or list of array w/o duplicates


# PRACTICE !!
# Q3: remove element
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's


# Q4: two sum
# inputs: array of int's and target int
# output: return index of items from array that sum to target


# PRACTICE !!
# Q5: longest_substring_no_duplicates
# input: string
# output: integer; length of longest non duplicated chars in string


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word


# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters


# PRACTICE !!
# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis


# PRACTICE !!
# Q9: search rotated array
# input: array sorted than can be rotated 'k' numbers, and a target integer
# output: Boolean to see if target is inside the rotated array


# PRACTICE !!
# Q10: sqrt
# input: integer x
# output: find the number that is the sqrt or closest sqrt of integer

###############################3

# Q1: single number
# input: array of integers with all nums having a duplicate except 1
# output: the single number in array that has no duplicates
def single_number(nums):
    s = set()
    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    return s.pop()



# Q2: remove duplicates:
# input: array of int's Sorted w/ or w/o duplicates
# output: int of length of array w/o duplicates or list of array w/o duplicates
def remove_duplicates(nums):
    left_index = 0
    
    for right_index in range(len(nums)-1 ):
        if nums[right_index] != nums[right_index + 1]:
            nums[left_index] = nums[right_index + 1]
            left_index += 1
            
    return nums[:left_index]



# Q3: remove element
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key_item):
    
    
    left_index = 0
    right_index = len(nums) - 1
    
    while left_index <= right_index:
        if nums[left_index] == key_item:
            nums[left_index] = nums[right_index]
            right_index -= 1
        else:
            left_index += 1
    return nums[:left_index]

        

# Q4: two sum
# inputs: array of int's and target int
# output: return index of items from array that sum to target
def two_sum(nums, target):
    d = dict()
    for i in range(len(nums) ):
        remain = target - nums[i]
        if remain in d:
            return d[remain], i
        else:
            d[nums[i] ] = i
            

# PRACTICE !!
# Q5: longest_substring_no_duplicates
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_duplicates(string1):
    s = set()
    left = 0        
    result = 0
    for right in range(len(string1) ):
        while string1[right] in s:
            s.remove(string1[left])
            left += 1
        s.add(string1[right] )
        result = max(right-left + 1)
        
    return result


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
def longest_prefix(words):
    result = ''
    shortest_word = math.inf
    
    for w in words:
        shortest_word = min(shortest_word, len(w) )
    
    i = 0
    while i < shortest_word:
        temp = words[0][i]
        for j in range( 1, len(words) ):
            if temp != words[j][i]:
                return result
        
        result += temp
    return result


# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    for w in words:
        ordered_w = "".join(sorted(w) )
        if ordered_w in d:
            d[ordered_w] += w
        else:
            d[ordered_w] = w
    return d.values()


# PRACTICE !!
# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    if len(string1) == 0:
        return True
    opened = ['(', '[', '{']
    
    closed = [')', ']', '}']
    stack = []
    
    for c in string1:
        if c in opened:
            stack.append(c)
        else:
            if len(stack) != 0 and stack[-1] == opened[closed.index(c)]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False
                

# PRACTICE !!
# Q9: search rotated array
# input: array sorted than can be rotated 'k' numbers, and a target integer
# output: Boolean to see if target is inside the rotated array
def search_sorted_array(nums, target):
    if len(nums) == 0:
        return False
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (right+left) // 2
        if nums[mid] == target:
            return True
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
# Q10: sqrt
# input: integer x
# output: find the number that is the sqrt or closest sqrt of integer
def sqrt(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (right + left) // 2
        
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
            
        elif mid*mid < x:
            left = mid + 1
            
        elif mid*mid > x:
            right = mid - 1
        


if __name__ == "__main__":
    print('start\n')
    
    