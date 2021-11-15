# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:43:06 2021

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
    
    for right in range(len(nums)-1 ):
        if nums[right] != nums[right+1]:
            nums[left] = nums[right+1]
            left += 1
            
    return nums[:left]


# Q3: remove element        #10min
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key):
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left] == key:
            nums[left] = nums[right]
            right -=1
        else:
            left += 1
            
    return nums[:left]

    
# Q4: two sum           #10min
# inputs: array of int's and target int
# output: return index of items from array that sum to target
def two_sum(nums, target):
    d = dict()
    
    for i in range(len(nums)-1):
        remain = target-nums[i]
        if remain in d:
            return d[remain], i
        else:
            d[nums[i]] = i
            
    return None


# Q5: longest_substring_no_duplicates       #10min
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_duplicates(str1):
    longest = 0
    s = set()
    left = 0
    right = left
    
    for right in range(len(str1) ):
        while str1[right] in s:
            s.remove(str1[left] )
            left += 1
        s.add(str1[right])
        longest = max(longest, right - left + 1)
        
    return longest


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
def longest_prefix(words):
    shortest = math.inf
    for w in words:
        shortest = min(shortest, len(w) )
    
    res = ''
    for i in range(shortest):
        temp = words[0][i]
        
        for j in range(1, len(words) ):
            if words[j][i] != temp:
                return res
        res += temp
        
    return res


# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    
    for w in words:
        temp = "".join(sorted(w) )
        
        if temp in d:
            d[temp] += w
        else:
            d[temp] = w
            
    return d.values()


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(str1):
    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    stack = []
    
    for c in str1:
        if c in opened:
            stack.append(c)
        else:
            if stack and stack[-1] == opened[closed.index(c)]:
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
            if nums[left] <= target <= nums[target]:
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
        mid = (right+left) // 2
        
        if mid*mid <= x < (mid+1)*(mid+1):
            return True
        
        elif mid*mid < x:
            left = mid + 1
            
        else:
            right = mid - 1
            
    return False
        

# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(expr):
    stack = []
    
    for c in expr:
        if c in "*+-/":
            right = stack.pop()
            left = stack.pop()
            
            if c == "+":
                stack.append(left+right)
            elif c == "-":
                stack.append(left-right)
            elif c == "*":
                stack.append(left*right)
            elif c == "/":
                stack.append(left/right(int))
        
        else:
            stack.append(int(c) )
        
        
# Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] == target:
            return left, right
        
        elif nums[left] + nums[right] > target:
            right -= 1
            
        else:
            left += 1
    
    return None


# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def number_of_islands(island):
    counter = 0
    
    def dfs_island(i, j):
        if i < 0 or j < 0 or i >= len(island) or j >= len(island) or island[i][j] != 1:
            return
        island[i][j] = 0
        
        dfs_island(i-1, j)
        dfs_island(i+1, j)
        dfs_island(i, j-1)
        dfs_island(i, j+1)
        
    
    for i in range(len(island) ):
        for j in range(len(island[0]) ):
            if island[i][j] == 1:
                dfs_island(i, j)
                counter += 1
    return counter
    


# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def contain_duplicates(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False


# Q15: move zeros
# input: given an array of numbers
# output: move all zeros to the end and edit nums array in place
def move_zeros(nums):
    left = 0
    zeros = 0
    
    for right in range(len(nums) ):
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
    right = len(word) - 1
    for i in range(len(word)//2 ):
        temp = word[left]
        word[left] = word[right]
        word[right] = temp
        left += 1
        right -= 1


# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersection_of_arrays(list1, list2):
    s = set(list1)
    res = []
    
    for n in list2:
        if n in s:
            s.remove(n)
            res.add(n)
            
    return res


# Q18: binary search
# input: 1-D array of integers and target goal
# output: boolean if found target within n
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (right+left) // 2
        
        if nums[mid] == target:
            return True
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
            
    return False
        

# Q19: first unique char
# input: given a string called string1 of letters
# output: return int index of first non-repeating char
def first_unique_char(str1):
    d = dict()
    
    for c in str1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for k,v in d.item():
        if v == 1:
            return str1.index(k)
        
    return -1


# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string
def decode_string(str1):
    res = ''
    cur_num = 0
    stack = []
    
    for c in str1:
        if c == '[':
            stack.append(res)
            stack.append(cur_num)
            res = ''
            cur_num = 0
            
        elif c == ']':
            prev_num = stack.pop()
            prev_str = stack.pop()
            res = prev_str + prev_num*res
            
        
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
    largest = 0
    
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
    prefix = 0
    tsum = sum(nums)
    
    for i in range(len(nums) ):
        if prefix == tsum - nums[i] - prefix:
            return i
        prefix += nums[i]
        
    return -1


# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def temperature_days(days):
    res = [0] * len(days)
    stack = []
    
    for i in range(len(days)):
        if stack and days[i] > days[stack[-1]]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
        
    return res



# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer
def largest_number_double_than_others(nums):
    max1 = -math.inf
    second = max1
    index = -1

    for i in range(len(nums)):
        if nums[i] >= max1:
            second = max1
            max1 = nums[i]
            index = i
            
        elif nums[i] >= second:
            second = nums[i]
    
    if max1 >= second*2:
        return index
    return -1



# Q25: jewels and stones
# input: string called jewels that contain char jewels and string called stones made of char's
# output: return integer of how many stones match the type of jewels
def jewels_stones(jewels, stones):
    s = set(jewels)
    counter = 0
    for c in stones:
        if c in s:
            counter += 1
    return counter


# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def keys_and_rooms(rooms):
    my_keys = []
    visited = set()
    stack = [0]
    
    while stack:
        cur = stack.pop()
        my_keys.append(cur)
        visited.add(cur)
        
        for i in rooms[cur]:
            if i not in visited:
                stack.append(i)
    
    return len(my_keys) == len(rooms)



# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
def square_sorted_array(nums):
    left = 0
    right = len(nums)-1
    index = right
    res = [0] * len(nums)
    
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            res[index] = nums[right]*nums[right]
            right -= 1
        else:
            res[index] = nums[left]*nums[left]
            left += 1
        index -= 1
    
    return res


# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030
def find_even_integer_nums(nums):
    counter = 0
    
    for i in nums:
        temp = 0
        while i:
            i = i // 10
            temp += 1
        
        if temp % 2 == 0:
            counter += 1
            
    return counter
            
            

# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums
def check_if_double(nums):
    s = set()
    
    for i in nums:
        if i*2 in s or (i%2 == 0 and i // 2 in s):
            return True
        s.add(i)
        
    return False



# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def maximum_size_subarray_sum_equals_k(nums, k):
    longest = 0
    prefix = 0
    d = dict()

    for i in range(len(nums) ):
        prefix += nums[i]
        
        if prefix == k:
            longest = i + 1
        
        if prefix - k in d:
            longest = max(longest, i - d[prefix - k])
         
        if prefix not in d:
            d[prefix] = i
            
    return longest



# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have at a time
# output: integer of the max length substring possible with k distict letters
def longest_substring_k_distinct_chars(s, k):
    longest = 0
    left = 0
    d = dict()
    
    for right in range(len(s) ):
        if s[right] in d:
            d[s[right]] += 1
        else:
            d[s[right]] = 1
        
        
        while left < right and len(d) > k:
            if d[s[left]] == 1:
                del d[s[left]]
            else:
                d[s[left]] -= 1
        
        longest = max(longest, right - left + 1)
        
    return longest



# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_sum_equals_k(nums, k):
    d = dict()
    prefix = 0
    count = 0
    
    for i in nums:
        prefix += i
        
        if prefix - k in d:
            count += d[prefix - k]
        
        if prefix in d:
            d[prefix] += 1
        else:
            d[prefix] = 1
            
    return count




# DO QUESTIONS_2.py !!!!!!

# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
def unique_path(m,n):
    dp = np.zeros( (m,n), dtype=int)+1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j]
    return dp[m-1][n-1]



# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subsequence(nums):
    dp = [0] * len(nums)
    
    for i in range(len(nums) ):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] =  max(dp[i], 1+dp[j])
    return max(dp)



# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums, k):
    def reverse(l, r):
        for i in range(len(nums) // 2):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
        
    
    k = k % len(nums)
    if len(nums) * k == 0:
        return
    
    reverse(0, len(nums)-1)
    reverse(0, k-1)
    reverse(k, len(nums) - 1)
    



# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def get_right_side_BST(root):
    queue = []
    res = []
    queue.append(root)
    
    while queue:
        row_len = len(queue)
        right_side = None
        
        for i in range(row_len):
            cur = queue.pop(0)
            if cur:
                right_side = cur
                queue.append(cur.left)
                queue.append(cur.right)
        
        if right_side:
            res.append(right_side.val)
    return res



            
            
            
    
    
    
            