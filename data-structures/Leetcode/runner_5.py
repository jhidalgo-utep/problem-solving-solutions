# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:10:00 2021

@author: joaqu
"""
import math

# PRACTICE 9, 20, 21, 23, 26

# Q1: single number
# input: array of integers with all nums having a duplicate except 1
# output: the single number in array that has no duplicates


# Q2: remove duplicates:
# input: array of int's Sorted w/ or w/o duplicates
# output: int of length of array w/o duplicates or list of array w/o duplicates


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


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis


# PRACTICE !!
# Q9: search rotated array
# input: array sorted than can be rotated left or right, and a target integer
# output: Boolean to see if target is inside the rotated array

# Q10: sqrt
# input: integer x
# output: find the number that is the sqrt or closest sqrt of integer


# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression


#Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result


# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands


# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not


# Q15: move zeros
# input: given an array of numbers
# output: move all zeros to the end and edit nums array in place


# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace


# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2


# Q18: binary search
# input: 1-D array of integers and target goal
# output: boolean if found target within n


# Q19: first unique char
# input: given string1 of letters
# output: return int index of first non-repeating char


# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string


# #Q21: max consecutive one's
# input: 1-D array of 1's and 0's 
# output: integer of the highest amount of consecutive one's


# Q22: find pivot
# input: takes in 1-D array of int's
# output: return int index that has the right and left side of pivot index equal each other


# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index


# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer


# Q25: jewels and stones
# input: string called jewels that contain char jewels and string called stones made of char's
# output: return integer of how many stones match the type of jewels


# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.


# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
# example: nums = [-8, -3, 0, 5, 10, 12]


# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030


# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums


#########################################################
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
    left = 1
    
    for i in range(nums):
        if nums[i] != nums[i+1]:
            nums[left] = nums[i+1]
            left += 1    
    return nums[:left]


# Q3: remove element
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] == key:
            nums[left] = nums[right]
            right -= 1
        else:
            left -= 1
            
    return nums[:left ]

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


# Q5: longest_substring_no_duplicates
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_dup(string1):
    s = set()
    longest = 0
    left = 0
    
    for i in range(len(string1) ):
        while string1[i] in s:
            s.remove(string1[left])
            left += 1
        s.add(string1[i])
        longest = max(longest, i - left + 1)
    return longest
            
                        
# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
def longest_prefix(words):
    
    min_length = math.inf
    for word in words:
        min_length = min(len(word), min_length)
        
    result = ''
    
    #iter the max possible length (checking char)
    for j in range(min_length):
        temp = ''
        temp = words[0][j]
        
        #iter through all words except the first word -} 'temp'  (checking words)
        for i in range(1, len(words) ):
            if temp != words[i][j]:
                return result
            
        result += temp
    
    return result



# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    # create data strcuture dict to contain key = ordered word and value = list of common words
    #iter thru words to either store or append to dict
    #return the (k,v) .values() of each 
    dictionary = dict()
    
    for word in words:
        temp = ''.join(sorted(word) )
        
        if temp in dictionary:
            d[temp] += word
        else:
            dictionary[temp] = word
                
    return dictionary.values()



# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    open_p = ['(', '{', '[']
    closed_p = [')', '}', ']']
    stack = []
    
    for i in range(len(strings1) ):
        if string1[i] in open_p:
            stack.append(string[i] )
        
        elif string1[i] in closed_p:
            if stack and stack[-1] == open_p[ closed_p.index(string1[i]) ]:
                stack.pop()
        
        else:
            return False
        
    return len(stack) == 0


# PRACTICE !!
# Q9: search rotated array
# input: array sorted than can be rotated left or right, and a target integer
# output: Boolean to see if target is inside the rotated array
def search_sorted_arr(nums, target):
    
    left = 0 
    right = len(nums) - 1
    
    while left <= right:
        mid = left+right // 2
        
        if nums[mid] == target:
            return True
        
        elif nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False
                
    
# Q10: sqrt
# input: integer x
# output: find the number that is the sqrt or closest sqrt of integer
def sqrt(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left+right) // 2
        
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
        
        elif mid*mid < x:
            left = mid + 1
        
        elif mid*mid > x:
            right = mid - 1
            

# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(exp):
    stack = []
    
    for i in exp:
        
        if i in "*+-/":
            right = stack.pop()
            left = stack.pop()
            
            if i == '-':
                stack.append(left-right)
            elif i == '+':
                stack.append(left+right)
            elif i == '*':
                stack.append(left+right)
            elif i == "/":
                stack.append( int(left//right) )
        else:
            stack.append( int(i) )
    
    return stack.pop()



#Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        temp_sum = nums[left]+nums[right]
        
        if temp_sum == target:
            return left, right
        
        elif temp_sum < target:
            left += 1
            
        elif temp_sum > target:
            right -=1
            

# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def num_of_islands(island):
    
    num_of_islands = 0
    
    for i in range(len(islands) ):
        for j in range( len(islands[0] )):
            if island[i][j] == 1:
                dfs_island(island, i, j)
                num_of_islands += 1
                
    return num_of_islands


def dfs_island(island, i , j):
    
    if i < 0 or i >= len(island) or j < 0 or j >= len(island[0] or island[i][j] != 1):
        return
    
    island[i][j] = 3
    
    dfs_island(island, i, j-1)
    dfs_island(island, i, j+1)
    dfs_island(island, i-1, j)
    dfs_island(island, i+1, j)
    
    


# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def contain_dup(nums):
    s = set()
    for i in nums:
        if i in s:
            return False
        else:
            s.add(i)
    
    return True


# Q15: move zeros
# input: given an array of numbers
# output: move all zeros to the end and edit nums array in place
def move_zeros(nums):
    left = 0
    zeros = 0
    
    for iter_index in range(len(nums) ):
        if nums[iter_index] == 0:
            zeros += 1
        else:
            nums[left] = nums[iter_index]
            left += 1
    
    for i in range(zeros):
        nums[-i-1] = 0


# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace
def reverse_string(word):
    
    if len(word) <= 1:
        return word
    
    left = 0
    right = len(word)
    
    while left < len(word) // 2:
        temp = word[right]
        word[right] = word[left]
        word[left] = temp
        left += 1
        right -= 1
    

# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersection_of_arrays(arr1, arr2):
    s = set(arr1)
    result = []
    
    for i in arr2:
        if i in s:
            result.append(i)
            s.remove(i)
            

# Q18: binary search
# input: 1-D array of integers and target goal
# output: boolean if found target within n
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        elif nums[mid] < target:
            left = mid + 1
        
        elif nums[mid] > target:
            right = mid - 1
        
        
    return False


# Q19: first unique char
# input: given a string called string1 of letters
# output: return int index of first non-repeating char
def first_unique_char(string1):
    d = dict()
    
    for i in range(len(string1) ):
        
        if string1[i] in d:
            d[string[i] ] += 1
        else:
            d[string1[i] ] = 1
        
    for k,v in d.items():
        if v == 1:
            return string1.index(k)
        

# PRACTICE !!
# Q20: decode string
# input: recieved a string made of nums and letters and brackets [, ]
# output: return string of decoded string
def decode_string(string1):
    
    curr_num = 0
    curr_string = ''
    stack = []
    
    for i in string1:
        if i.is_digit():
            curr_num = curr_num*10 + int(i)
        
        elif i == '[':
            stack.append(curr_num)
            stack.append(curr_string)
            curr_num = 0
            curr_string = ''
        
        elif i == ']':
            prev_string = stack.pop()        
            prev_num = stack.pop()
            curr_string = prev_string + prev_num*curr_string
        
        else:
            curr_sting += i
    
    return curr_string


# PRACTICE !!
# #Q21: max consecutive one's
# input: 1-D array of 1's and 0's 
# output: integer of the highest amount of consecutive one's
def consecutive_ones(nums):
    highest = 0
    consec = 0
    
    for i in nums:
        if i == 1:
            consec += 1
        else:
            hightest = max(consec, highest)
            consec = 0
    
    hightest = max(consec, highest)
    return highest


# Q22: find pivot
# input: takes in 1-D array of int's
# output: return int index that has the right and left side of pivot index equal each other
def find_pivot(nums):
    if len(nums) <= 2:
        return -1
    
    t_sum = sum(nums)
    left_sum = 0
    
    for i in range(len(nums) ):
        if left_sum == t_sum - left_sum - nums[i]:
            return i
        
        left_sum += nums[i]
    
    return -1


# PRACTICE !!
# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def daily_temperature(nums):
    result = [0] * len(nums)
    stack = []
    
    for i in range(len(nums) ):
        while stack and nums[i] > nums[ stack[-1] ]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
            
        stack.append(i)
    
    return result


# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer
def largest_double_all_nums(nums):
    first = -math.inf
    second = -math.inf
    index = -1
    
    for i in range( len(nums) ) :
        if nums[i] > first:
            second = first
            first = nums[i]
            index = i 
        
        elif nums[i] > second:
            second = nums[i]
    
    if first >= second*2:
        return index
    return -1



# Q25: jewels and stones
# input: string called jewels that contain char jewels and string called stones made of char's
# output: return integer of how many stones match the type of jewels
def jewels_stones(jewels, stones):
    s = set(jewels)
    counter = 0
    for i in stones:
        if i in s:
            counter += 1
    return counter
            
    
# PRACTICE !!
# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def keys_and_rooms(rooms):
    s = set()
    stack = []
    stack.append(0)
    
    while stack:
        curr = stack.pop() 
        s.add(curr )
        
        for k in rooms[curr]:
            if k not in s:
                stack.append(k)
                
    return len(s) == len(rooms)


# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
# example: nums = [-8, -3, 0, 5, 10, 12]

def sorted_arr_squares(nums):
    
    left = 0
    right = len(nums)-1
    result = [0] * len(nums)
    index = right
    
    while left <= right:
        temp_num = 0
        
        if abs(nums[left]) > abs(nums[right] ):
            temp_num = nums[left]*nums[left]
            left += 1
            
        else:
            temp_num = nums[right]*nums[right]
            right -= 1
        
        result[index] = temp_num
        index -= 1
    
    # result[index] = nums[left]*nums[right]
    
    return result
            
  
    
# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030
def count_even_numbers(nums):
    counter = 0
    
    for i in nums:
        temp = 0 
        while i > 0:
            temp += 1
            i = i // 10
        
        if temp % 2 == 0:
            counter += 1
    
    return counter


# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums
def check_double_exists(nums):
    if len(nums) <= 1:
        return False
    
    s = set()
    
    for i in nums:
        if i*2 in s or (i % 2 == 0 and (i // 2) in s):
            return True
        
        s.add(i)
        
    return False
        
        
    
    
            
    
    
    
    
    

if __name__ == "__main__":
    print('start\n')
    
    # q6 = ['soccer', 'socks', 'socket']
    # q6_result = longest_prefix(q6)
    # print( q6_result )
    

    # q15 = [5,0,10,11,17,0,0,0,22,0,4,0]
    # move_zeros(q15)
    # print(q15)


    q27 = [-4, -2, 0, 3, 9, 12]
    print( sorted_arr_squares(q27) )
    
    
    
    