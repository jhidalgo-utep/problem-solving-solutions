# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:20:00 2021

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
# input: given a string called string1 of letters
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



# Q1: single number
# input: array of integers with all nums having a duplicate except 1
# output: the single number in array that has no duplicates
def single_num(nums):
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
def remove_dup(nums):
    left = 1
    for right in range(len(nums)- 1):
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
            left += 1
    
    return nums[:left]



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
    return None


# Q5: longest_substring_no_duplicates
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring(string1):
    s = set()
    left = 0
    longest = 0
    
    for i in range(len(string1) ):
        while string1[i] in s:
            s.remove(string1[left] )
            left += 1
        s.add(string1[i] )
        longest = max(longest, i - left + 1)
        
    return longest


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
def longest_prefix(words):
    shortest_word = 0
    for w in words:
        shortest_word = min(len(w), shortest_word)
    
    prefix = ''
    
    for i in range(shortest_word ):
        temp = word[0][i]
        
        for j in range(1, len(words) ):
            if words[j][i] != temp:
                return result
            
        prefix += temp
    return prefix
            

# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    
    for word in words:
        w = ''.join(sorted(word) )
        if w in d:
            d[w] += word
        else:
            d[w] = word
            
    return d.values()


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    opened = ['(', '{', '[']
    closed = [')', '}', ']']
    stack = []
    
    for i in string1:
        if i in opened:
            stack.append(i)
        
        elif i in closed:
            if stack and stack[-1] == opened[closed.index(i) ]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


# Q9: search rotated array
# input: array sorted than can be rotated left or right, and a target integer
# output: Boolean to see if target is inside the rotated array
def search_rotated_array(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left+right) // 2
        
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
    return


# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(expr):
    stack = []
    
    
    for i in expr:
        
        if i.is_digit():
            stack.append(int(i) )
        else:
            right = stack.pop()
            left = stack.pop()
        
            if i in "*-+/":
                
                if i == "+":
                    stack.append( left+right )
                
                elif i == "-":
                    stack.append( left - right )
                
                elif i == "*":
                    stack.append( left*right )
                
                elif i == "/":
                    stack.append( int( (left+right)//2) )

    return stack.pop()            
            
        
#Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] + nums[right] == target:
            return left,right
        
        elif nums[left] + nums[right] < target:
            left += 1
        
        elif nums[left] + nums[right] > target:
            right -= 1
            
    return 
    

# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def num_of_islands(grid):
    result = 0
    
    for i in range(len(grid) ):
        for j in range(len(grid[0]) ):
            if grid[i][j] == 1:
                result += 1
                dfs_island(grid, i, j)
    return result

def dfs_island(grid, i, j):
    
    if i < 0 or j < 0 or i > len(grid) or j > len(grid[0]) or grid[i][j] != 1:
        return 
    
    grid[i][j] = 2
    
    dfs_island(grid, i, j-1)
    dfs_island(grid, i, j+1)
    dfs_island(grid, i+1, j)
    dfs_island(grid, i-1, j)
    


# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def contain_dup(nums):
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
    zeros = 0
    left = 0
    
    for right in range(len(nums) ):
        if nums[right] == 0:
            zeros += 1
        else:
            nums[left] = nums[right]
            left += 1
    
    for i in range(zeros):
        nums[-i-1] = 0
        


# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace
def reverse_string(word):
    
    if len(word) <= 1:
        return
    
    right = len(word) - 1
    
    for i in range(len(word) // 2):
        temp = word[i]
        word[i] = word[right]
        word[right] = temp
        right -=1
    


# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersection(arr1, arr2):
    s = set(arr1)
    result = []
    
    for j in arr2:
        if j in s:
            result.append(j)
            s.remove(j)
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
            left = mid + 1
        
        elif nums[mid] > target:
            right = mid -1
            
    return False
        

# Q19: first unique char
# input: given a string called string1 of letters
# output: return int index of first non-repeating char
def first_uniq_char(string1):
    d = dict()
    
    for i in string1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for j in d.values():
        if j == 1:
            return string1.index(j)
        

# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string
def decode_string(string1):
    curr_num = 0
    curr_str = ''
    
    for i in string1:
        if i == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ''
            curr_num = 0
        
        elif i == ']':
            prev_num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + prev_num*curr_str
            
        
        elif i.is_digit():
            curr_num = curr_num*10 + int(i)
        
        else:
            curr_str += i
    
    return curr_str
            


# #Q21: max consecutive one's
# input: 1-D array of 1's and 0's 
# output: integer of the highest amount of consecutive one's
def max_consec_ones(nums):
    consec = 0
    longest = 0
    
    left = 0
    
    for right in range(len(nums) ):
        if nums[right] == 0:
            consec = 0
        else:
            consec += 1
        longest = max(consec, longest)
    return longest



# Q22: find pivot
# input: takes in 1-D array of int's
# output: return int index that has the right and left side of pivot index equal each other
def find_pivot(nums):
    left_sum = 0
    t_sum = sum(nums)
    
    for i in range(nums):
        if t_sum - left_sum - nums[i] == left_sum:
            return i
        else:
            left_sum += nums[i]
    return -1



# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def temperature(nums):
    stack = []
    result = [0] * len(nums)
    
    for i in range(len(nums) ):
        while stack and nums[i] > nums[ stack[-1] ]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    
    return result


# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer
def largest_num_double(nums):
    first = -math.inf
    second = first
    index = -1
    
    for i in range(len(nums) ):
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


# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def key_room(rooms):
    s = set()
    stack = []
    stack.append(0)
    
    while stack:
        curr = stack.pop()
        s.add(curr)
        
        for i in rooms[curr]:
            if i not in s:
                stack.append(i)
                
    return len(s) == len(rooms)
                


# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
# example: nums = [-8, -3, 0, 5, 10, 12]
def squares_sorted(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    index = right
    
    while left <= right:
        
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] * nums[left]
            left += 1
        else:
            result[index] = nums[right] * nums[right]
            right -= 1
            
        index -= 1
    
    return result




# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030
def even_num_integers(nums):
    counter = 0
    
    for i in nums:
        temp = 0
        
        while i > 0:
            i = i // 10
            temp += 1
        
        if temp % 2 == 0:
            counter += 1
            
    return counter
            

# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums
def check_if_double_exist(nums):
    s = set()
    
    for i in nums:
        if nums*2 in s or (i%2==0 and i // 2 in s):
            return True
        s.add(i)
    return False




if __name__ == "__main__":
    print('start')
    
    q21 = [1,1,1,0,0,1,1,0,1,1,1,1]
    print(max_consec_ones(q21) )
    
    