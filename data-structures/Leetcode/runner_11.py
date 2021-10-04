# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:45:28 2021

@author: joaqu
"""
import numpy as np
import heapq


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
    for i in range(len(nums) - 1):
        if nums[i] != nums[i+1]:
            nums[left] = nums[i+1]
            left += 1
    return nums[:left]
            


# Q3: remove element
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key):
    left = 0
    right = len(nums)-1
    
    while left < right:
        if nums[left] == key:
            nums[left] = nums[right]
            right -= 1
        else:
            left +=1
    return nums[:left]



# Q4: two sum
# inputs: array of int's and target int
# output: return index of items from array that sum to target
def two_sum(nums, target):
    d = dict()
    
    for i in range(len(nums) ):
        remain = target - nums[i]
        if remain in d:
            return i, d[remain]
        else:
            d[nums[i]] = i
            
            
# Q5: longest_substring_no_duplicates
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_duplicates(string1):
    s = set()
    left = 0
    longest = 0
    
    for c in range(len(string1) ):
        while string1[c] in s:
            s.remove(string1[left])    
            left += 1
        s.add(string1[c] )
        longest = max(longest, c-left+1)
    return longest


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
def longest_prefix(words):
    shortest = len(words[0])
    for word in words:
        shortest = min(shortest, len(word) )
    
    res = ''
    for i in range(shortest):
        temp_char = words[0][i]
        
        for j in in range(1, len(words)):
            if words[j][i] != temp_char:
                return res
        res += temp_char
    return res
        

# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    res = []
    
    for word in words:
        ow = "".join(sorted(word))
        if ow in d:
            d[ow] += word
        else:
            d[ow] = word
    
    return d.values()


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    opened = ["(", "[", "{"]
    closed = [")", "]", "}"]
    stack = []
    
    for i in string1:
        if i in opened:
            stack.append(i)
        
        else:
            if stack and stack[-1] == opened[ closed.index(i) ]:
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
        mid = (right + left) // 2
        
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
        mid = (right+left) // 2
        
        if mid*mid <= x < (mid+1)*(mid+1):
            return True
        
        if mid*mid < x:
            left = mid + 1
            
        elif mid*mid > x:
            right = mid - 1
    return False



# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(nums):
    stack = []
    
    for c in nums:
        if c in "+-*/":
            right = stack.pop()
            left = stack.pop()
            
            if c == "-":
                stack.append( left - right)
            elif c == "+":
                stack.append(left+right)
            elif c == "*":
                stack.append(left*right)
            elif c == '/':
                stack.append( left // right )
        else:
            stack.append(int(c) )
                
    return stack.pop()
    
    

#Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] == target:
            return left,right
        
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
            
    return None


# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def number_of_islands(board):
    counter = 0
    for i in range(len(board) ):
        for j in range(len(board[0]) ):
            if board[i][j] == 1:
                dfs_island(board, i, j)
                counter += 1
    return counter


def dfs_island(board, i, j):
    if i<0 or j<0 or i >= len(board) or j >= len(board[0]) or if board[i][i] != 1:
        return
    
    board[i][j] = 0
    
    dfs_island(board, i-1, j)
    dfs_island(board, i+1, j)
    dfs_island(board, i, j-1)
    dfs_island(board, i, j+1)



# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def contains_dup(nums):
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
    zeros = 0
    left = 0
    
    for i in nums:
        if i != 0:
            nums[left] = i
            left += 1
        else:
            zeros += 1
    
    for i in range(zeros):
        nums[-1-i] = 0



# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace
def reverse_string(letters):
    right = len(letters) - 1
    
    for i in range(len(letters) // 2):
        temp = letters[i]
        letters[i] = letters[right]
        letters[right] = temp



# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersect_arrays(list1, list2):
    s = set(list1)
    res = []
    for i in list2:
        if i in s:
            res.append(i)
            s.remove(i)
            
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
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
            
# Q19: first unique char
# input: given a string called string1 of letters
# output: return int index of first non-repeating char
def first_unique_char(string1):
    d = dict()
    
    for i in range(len(string1) ):
        if string1[i] in d:
            d[string1[i]] += 1
        else:
            string1[i] = 1
            
    for k,v in d.items():
        if v == 1:
            return string1.index(k)
    return None


# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string
def decode_string(string1):
    
    cur_num = 0
    res = ''
    stack = []
    
    for c in string1:
        if c.is_digit():
            cur_num = int(c)
        
        if c == '[':
            stack.append(res)
            stack.append(cur_num)
            res = ''
            cur_num = 0
        
        elif c == ']':
            prev_num = stack.pop()
            prev_str = stack.pop()
            res = prev_str + res*prev_num
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
    t_sum = sum(nums)
    prefix = 0
    for i in nums:
        if t_sum - prefix - i == prefix:
            return i
        prefix += i
        
    return -1



# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def temperature(nums):
    res = [0] * len(nums)
    stack = []
    
    for i in range(len(nums) ):
        while stack and nums[stack[-1]] < nums[i]:
            pos = stack.pop
            res[0] = i - pos
        stack.append(i)
    
    return res
    



       


##############################################################################

# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def maximum_subarray_to_k(nums, k):
    d = dict()
    longest = 0
    prefix_sum = 0
    
    for i in range(len(nums)):
        prefix_sum += nums[i]
        
        if prefix_sum == k:
            longest = i + 1
        
        if prefix_sum - k in d:
            longest = max(longest, i - d[prefix_sum - k] )
        
        if prefix_sum not in d:
            d[prefix_sum] = i
        
    



# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have in dict
# output: integer of the max length substring possible with k distict letters
def longest_substring_with_k_distinct_letters(s, k):
    n = len(s)
    if n*k == 0:
        return 0
    d= dict()
    res = 0
    left = 0
    
    for right in range(n):
        if s[right] in d:
            d[s[right]] += 1
        else:
            d[s[right]]= 1
        
    
        while left < right and len(d) > k:
            if d[s[left]] == 1:
                del d[s[left]]
            else:
                d[s[left]] -= 1
        
        res = max(res, right-left+1)
        
    return res


# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_sum_k(nums, k):
    prefix_sum = 0
    d = dict()
    count = 0
    
    for i in nums:
        prefix_sum += i
        
        if prefix_sum - k in d:
            count += d[prefix_sum - k]
        
        if d[prefix_sum] in d:
            d[prefix_sum] += 1
        else:
            d[prefix_sum] = 1
            
    return count
            
        

# Q4: Sliding Window Maximum
# input: 1-d array of integers and integer 'k' that is the size of the window
# output: integer array of the all the maximum int's at each combination subarray of size k
def sliding_window(nums, k):
    left = 0
    result = []
    dq = []  #indices : dq[0] large --- dq[-1] small
    
    for right in range(len(nums) ):
        while dq and nums[dq[1]] <= nums[right]:
            dq.pop(-1)
        
        dq.append(right)
        
        if left > dq[0]:
            dq.pop()
        
        if right + 1 >= k:
            result.append(nums[dq[0]])
            left += 1
            
    return result
    


# Q5: Top K frequent words
# input: 1-D array of string words and integer k for the amount of top freq. words
# output: a list of the top 'k' frequent words
def k_frequent_words(words, k):
    d = dict()
    res = []
    
    for word in words:
        if word in d:
            d[word] -= 1
        else:
            d[word] = -1
    
    h1 = = []
    for key, v in d.items():
        heapq.heappush(h1, (v,key))
    
    for i in range(k):
        res.append(heapq.heappop(h1) )
    return res


# Q6: is palidrome (integer)
# input: integer above zero
# output: boolean determining if integer is palidrome or not
def is_palindrome(num):
    if num < 0:
        return False
    if num > 0 and num % 10 == 0:
        return False
    
    rev_num = 0
    
    while rev_num < num:
        rev_num = (rev_num*10) + num%10
        num = num // 10
    
    if rev_num == num or rev_num // 10 == num:
        return True
    return False







######################################################################3

# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_sum_subarray(nums):

    dp = [0]*len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums) ):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        
    return max(dp)

# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l = i +1
        r = len(nums) - 1
        
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                res.append( nums[i] + nums[l] + nums[r] )
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    left += 1
            
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
                
            else:
                r -= 1
                
    return res
            



# Q4: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_1(nums):
    min1 = math.inf
    max_profit = 0
    for i in nums:
        if i < min1:
            min1 = i
        max_profit = max(max_profit, i - min1)
    return max_profit
        


# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_2(nums):
    max_profit = 0
    
    for i in range(len(nums)-1 ):
        if nums[i+1] > nums[i]:
            max_profit += nums[i+1] - nums[i]
            
    return max_profit


# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_integer(num):
    if num < 0:
        symbol = -1
        num = num * -1
    else:
        symbol = 1
        
    result = 0
    
    while num:
        result = (result * 10) + (num % 10)
        num = num // 10
    
    if result > math.pow(2,31):
        return False
    
    if symbol == 1:
        return num
    return num * symbol



# Q7: is anagram
# input: 2 strings that represent words
# output: boolean checking if word 's' is anagram of word 't'
def anagram(s, t):
    if len(s) != len(t):
        return False
    
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for c in t:
        if c in d:
            d[c] -= 1
        else:
            return False
    
    for k,v in d.items():
        if v != 0:
            return False
    return True


# Q8: is palindrome
# input: string called 's' with spaces, nums, special chars
# output: return boolean if string is palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        while not s[left].isalnum() and left<right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    return True



# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    forward = 2
    backward = 1
    
    for i in range(n-2):
        temp = forward 
        forward = forward + backward
        backward = temp



# Q10: fibonacci sequence (O(1) space)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo2(n):
    forward = 1
    backward = 0
    
    for i in range(n-1):
        temp = forward
        forward = forward + backward
        backward = temp
        
    return forward



# Q11: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # return fibo(n-1) + fibo(n-2)
    if n == 0:
        return 0
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i] + dp[i-2]
    return dp[n]


# Q12: house robber
# input: 1-d array of integers that represent how much money each house has acording to its position
# output: integer, the maximum money that can be stolen not robing house directly next to each other
def house_robber(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums) ):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    
    return max(dp)


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_string(string1):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    res = 0
    for i in range(len(string1) ):
        if i + 1 < len(string1) and string1[i] < string1[i+1]:
            res -=  roman[string1[i] ]
        else:
            res += roman[string1[i] ]
            
    return res
        

# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def integer_to_roman(num):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    res = ''
    i = 0
    while num:
        res += (num // int_val[i]) * roman[i]
        num = num % int_val[i]
        i+= 1
    return res
    
    # for i in range(len(int_val) ):
    #     res += (num // int_val[i]) * roamn[i]
    #     num = num % int_val[i]
        
    # return res

# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triange(num_rows):
    res = [ [1] ]
    
    for i in range(1, num_rows):
        row = []
        prev = [0] + res[-1] + [0]
        
        for j in range(len(res[-1] ) + 1 ):
            row.append(prev[j] + prev[j+1] )    
        res.append(row)
        
    return res
    


# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_number(nums):
    n = len(nums)
    t_sum = sum(nums)
    return ( (n*(n+1)) // 2) - t_sum



# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def container_water(nums):
    left = 0
    right = len(nums) - 1
    max_water = 0
    
    while left < right:
        if nums[left] < nums[right]:
            max_water = max(max_water, (right-left) * nums[left] )
            left += 1
        else:
            max_water = max(max_water, (right-left) * nums[right] )
            right -= 1
            
    return max_water
        



# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_matrix(matrix):
    
    row_z = len(matrix) * [False]
    col_z = len(matrix[0]) * [False]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_z[i] = True
                col_z[i] = True
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row_z[i] == True or col_z[j] = True:
                matrix[i][j] = 0
    
                


# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palindrome(s):
    longest = 0
    res = ''
    
    for i in range(len(s) ):
        # ODD
        left = i
        right = left
        
        while left > 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    res = s[left:right+1]
                    longest = right - left + 1
                left -= 1
                right += 1
        
        #EVEN
        left = i
        right = i+1
        
        while left > 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1        
    return res
            


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
def median_data_stream(nums):
    hmin = hmax = []
    
    #  8, 4           11, 24
    for i in nums:
        heaqp.heappush(hmin, i)
        
        if len(hmin) > 0 and len(hmin) > 0 and hmin[0] < -1 * hmax[0]:
            v1 = -1* heapq.heappop(hmax)
            heapq.heappush(hmin, v1)
        
        if len(hmin) > (hmax) + 1:
            v1 = heapq.heappop(hmin)
            heaqp.heappush(hmax, -1* v1)
        
        if len(hmax) > len(hmin) + 1:
            v1 = -1* heapq.heappop(hmax)
            heapq.heappush(v1)
    
    if len(hmin) == len(hmax):
        v1 = heaqp.heappop(hmin) 
        v1 += heapq.heappop(hmax)
        v1 = v1 // 2
        return v1
    
    elif len(hmin) > len(hmax):
        return heapq.heappop(hmin)
    else:
        return -1*heapq.heappop(hmax)
    
        
        
        
    



# Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    
    path = set()
    
    def dfs_board(l,r, cur_len):
        if l < 0 or r < 0 or l >= len(board) or r >= len(board[0] or word[cur_len] != board[l][r] or (l,r) in path)
            return False
        
        path.add( (l,r) )
        res = ( dfs_board(i-1,j, cur_len +1 ) or
               dfs_board(i+1,j, cur_len +1 ) or
               dfs_board(i,j-1, cur_len +1 ) or
               dfs_board(i,j+1, cur_len +1 ) )
        path.remove( (i,j) )
        return res
        
    for i in range(len(board) ):
        for j in range(len(board[0] ) ):
            if dfs_board(i,j, 0):
                return True
    return False



# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_word(string1):
    res = 0
    in_word = False
    for c in string1:
        if c != ' ' and in_word == False:
            res += 1
            in_word = True
        
        elif c == ' ' and in_word == True:
            in_word = False
    return res



# Q23: t9 text letter possibility combinations
# input: a string representing a number
# output: a list of string combinations made from the input representing a number
def t9_combo(string1):
    phone = {"2":"abc", 
             "3":"def",
             "4":"ghi",
             "5":"jkl",
             "6":"mno",
             "7":"pqrs",
             "8":"tuv",
             "9":"wxyz" }
    
    stack = []
    stack.append( (0,"") )
    res = []
    
    while stack:
        cur_len, combo = stack.pop()
        
        if cur_len == len(string1):
            res.append(combo)
        else:
            next_digit = string1[cur_len]
            children = d[next_digit]
            for child in children:
                stack.append(cur_len + 1, combo+child)
                
    return result
            


# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def find_k_largest_element(nums, k):
    h1 = []
    
    for i in nums:
        heapq.heapush(h1, -1* i)
    
    val = None
    for i in range(k):
        val = heapq.heappop()
    return val


# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def top_k_freq_items(nums, k):
    d = dict()
    result = [] 
    
    for i in nums:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1
            
    h1 = []
    
    for key, v in d.items():
        heapq.heappush(h1, (v, key) )
    
    count = 0
    while count < k:
        count += 1
        freq, word = heapq.heappop()
        result.append(word)
        
    return result
        

# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def peak_mountain(nums):
    l = 0
    r = len(nums) - 1
    
    while l < r:
        mid = (r+l) // 2
        
        if nums[mid+1] > nums[mid]:
            l = mid+1
        else:
            r = mid
    
    return l
            



# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
def find_unique_path(m, n):
    dp = np.zeros( (m,n), dtype=int)+1
    
    for i in range( 1, len(m) ):
        for j in range( 1, len(n) ):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[m-1][n-1]


# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subsequence(nums):
    
    longest = 0
    dp = [1] * len(nums)
    
    for i in range(1, len(nums) ):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)



# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums, k):
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    
def reverse(nums,l,r):
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        
        l += 1
        r += 1


# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def right_side_BST(root):
    queue = [] #queue used for level order traversal
    queue.append(root)
    result = []
    
    while queue:
        node_length = len(queue)
        right_side = None
        
        for i in range(node_length):
            curr = queue.pop(0)
            if curr:
                right_side = curr
                stack.append(curr.left)
                stack.append(curr.right)
            
        if right_side:
            result.append(right_side)
    
    return result
        
        