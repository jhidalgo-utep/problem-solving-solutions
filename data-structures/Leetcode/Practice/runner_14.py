# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:55:27 2021

@author: joaqu
"""

# Q1: single number         #1min
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


# Q2: remove duplicates:        #7min
# input: array of int's Sorted w/ or w/o duplicates
# output: int of length of array w/o duplicates or list of array w/o duplicates
def remove_duplicates(nums):
    left = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[left] = nums[i+1]
            left += 1
    return nums[left]


# Q3: remove element        #10min
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key):
    # left = 0
    # for right in range(len(nums)):
    #     if nums[right] != key:
    #         nums[left] = nums[right]
    #         left += 1
            
    # return nums[:left]
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == key:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1
    return nums[:left]
    
            


# Q4: two sum           #10min
# inputs: array of int's and target int
# output: return index of items from array that sum to target
def two_sum(nums, target):
    d = dict()
    
    for i in range(len(nums)):
        if target-nums[i] in d:
            return d[target-nums[i]], i
        else:
            d[nums[i]] = i
            
    return None

# Q5: longest_substring_no_duplicates       #10min
# input: string
# output: integer; length of longest non duplicated chars in string
def longst_substring_no_dulicates(string1):
    s = set()
    longest= 0
    left = 0
    for i in range(len(string1)):
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
    shortest_word = math.inf
    for w in words:
        shortest_word = min(shortest_word, len(w))
    
    res = ''
    for i in range(shortest_word):
        temp = words[0][i]
        for j in range(1, len(words)):
            if words[j][i] != temp:
                return res
        res += temp
        
    return res



# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    
    for word in words:
        temp = ''.join(sorted(word))
        if temp in d:
            d[temp] += word
        else:
            d[temp] = word
    
    return d.values()


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    opened = ['(', '{', '[']
    closed = [')', '}', ']']
    stack = []
    
    for c in string1:
        if c in opened:
            stack.append(c)
        else:
            if stack and stack[-1] == closed[opened.index(c)]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

# Q9: search rotated array
# input: array sorted than can be rotated left or right, and a target integer
# output: Boolean to see if target is inside the rotated array
def search_sorted_array(nums, target):
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
    if x < 0:
        return 
    
    left = 0
    right = x
    while left <= right:
        mid = (left+right) // 2
        
        if mid*mid<= x < (mid+1)*(mid+1):
            return mid
        
        elif mid*mid < x:
            left = mid + 1
        else:
            right = mid - 1


# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(expr):
    stack = []
    
    for c in expr:
        if c in "+-*/":
            right = stack.pop()
            left = stack.pop()
            if c == '-':
                stack.append(left-right)
            elif == "+":
                stack.append(left + right)
            elif "*":
                stack.append(left*right)
            elif "/":
                stack.append(left//right)
        else:
            stack.append(int(c) )
    return stack.pop()
            


# Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] == target:
            return left, right
        
        elif nums[left] + nums[right] < target:
            left += 1
        
        elif nums[left] + nums[right] > target:
            right -= 1
    return Nones


# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def num_islands(island):
    counter = 0
    for i in range(len(island)):
        for j in range(len(island[0])):
            if island[i][j] == 1:
                dfs_island(island, i, j)
                counter += 1 
    return counter

def dfs_island(island, i, j):
    if i < 0 or j < 0 or i >= len(island) or j >= len(island[0]) or island[i][j] != 1:
        return False
    
    island[i][j] = 0
    
    dfs_island(island, i-1, j)
    dfs_island(island, i+1, j)
    dfs_island(island, i, j-1)
    dfs_island(island, i, j+1)
    


# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def contain_duplicates(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False


# Q15: move zeros
# input: given an array of numbers
# output: move all zeros to the end and edit nums array in place
def move_zeros(nums):
    left = 0
    zeros = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        else:
            zeros += 1
    
    for i in range(zeros):
        nums[-1-i] = 0
        


# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace
def reverse_string(word):
    left = 0
    right = len(word)
    
    while left < len(word) // 2:
        temp = word[left]
        word[left] = word[right]
        word[right] = temp
        left += 1
        right -= 1
    


# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersection_of_arrays(list1, list2):
    result = []
    s = set(list1)
    
    for i in list2:
        if i in s:
            res.append(i)
            s.remove(i)
            
    return result


# Q18: binary search
# input: 1-D array of integers and target goal
# output: boolean if found target within n
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left += 1
        elif nums[mid] > target:
            right -= 1
            
    return False
        

# Q19: first unique char
# input: given a string called string1 of letters
# output: return int index of first non-repeating char
def first_unique_char(string1):
    d = dict()
    
    for i in string1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for k,v in d.items():
        if v == 1:
            return string1.index(k)


# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string
def decode_string(string1):
    res = ''
    cur_num = 0
    stack = []
    
    for c in string1:
        if c == '[':
            stack.append(cur_num)
            stack.append(res)
            cur_num = 0
            res = ''
        elif c == ']':
            prev_string = stack.pop()
            prev_num = stack.pop()
            res = prev_string + prev_num*res
        elif c.is_digit():
            cur_num = int(c)
        else:
            res += c
            
    return res
        




# #Q21: max consecutive one's
# input: 1-D array of 1's and 0's 
# output: integer of the highest amount of consecutive one's
def max_consec_ones(nums):
   consec = 0
   highest = 0
   
   for i in nums:
       if i == 1:
           consec += 1
       else:
           consec = 0
       longest = max(longest, consec)
   return longest


# Q22: find pivot
# input: takes in 1-D array of int's
# output: return int index that has the right and left side of pivot index equal each other
def find_pivot(nums):
    left_side = 0
    tsum = sum(nums)
    
    for i in nums:
        if left_side == tsum - left_side - i:
            return True
        left_side += i
    return False
        

# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def temperatures(nums):
    stack = []
    res = [0] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)
    return res


# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer
def largest_number_double(nums):
    index = 0
    largest = 0
    second = 0
    
    for i in range(len(nums)):
        if nums[i] >= largest:
            second = largest 
            largest = nums[i]
            index = i
            
        elif num[i] >= second:
            second = nums[i]
    
    if first >= second*2:
        return index
    return -1
    


# Q25: jewels and stones
# input: string called jewels that contain char jewels and string called stones made of char's
# output: return integer of how many stones match the type of jewels
def jewels_and_stones(jewels, stones):
    counter = 0 
    s = set(jewels)
    for i in stones:
        if i in s:
            counter += 1
    return counter
    

# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def keys_rooms(rooms):
    s = set()
    stack = []
    stack.append(0)
    
    while stack:
        cur = stack.pop()
        s.add(curr)
        for i in rooms[curr]:
            if i not in s:
                stack.append(i)
    return len(s) == len(rooms)



# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
def square_sorted_array(nums):
    result = [0] * len(nums)
    
    left = 0
    right = len(nums) - 1
    cur_index = 0
    
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result[cur_index] = nums[right]*nums[right]
            right -= 1
        else:
            result[cur_index] = nums[left]*nums[left]
            left += 1
        cur_index += 1
    
    return result

        
        
        
# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030
def find_numbers_even_digits(nums):
    counter = 0
    for i in nums:
        if i>= 0 and i < 10:
            continue
        temp = 0
        while i:
            i = i // 10
            temp += 1
        
        if temp % 2 == 0:
            conter += 1
            
    return counter
        
        
        
# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums
def check_if_double_exist(nums):
    s = set()
    for n in nums:
        if n // 2 in s or n*2 in s:
            return True
        s.add(n)
    return False



# 3
# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def keys_rooms(rooms):
    stack = []
    stack.append(0)
    s = set()
    
    while stack:
        cur = stack.pop()
        s.add(cur)
        
        for i in rooms[cur]:
            if not i in s:
                stack.append(i)
    return len(s) == len(rooms)
                










if __name__ == "__main__":
    print('start')

    # q29 = [9, 8, 7, 14]
    # print( check_if_double_exist(q29) )
    
    print(401 % 100)


