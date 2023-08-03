from collections import deque
from typing import List
import re

def maxProfit(prices: List[int]) -> int:
    current_stock = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if(current_stock > prices[i]):
            current_stock = prices[i]
        if(prices[i] - current_stock > profit):
            profit = prices[i] - current_stock
    return profit

def removeElement(nums: List[int], val: int) -> int:
    # Counter for keeping track of elements other than val
    count = 0
    # Loop through all the elements of the array
    for i in range(len(nums)):
        if nums[i] != val:
            # If the element is not val
            nums[count] = nums[i]
            count += 1
    return count

def removeElement2(nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)  

def strStr(haystack: str, needle: str) -> int:
    index = 0
    first = needle[0]
    while(index < len(haystack)):
        if(haystack[index] == first and len(haystack[index:]) >= len(needle)):
                for i in range(len(needle)):
                    if(haystack[index + i] != needle[i]):
                        break
                    if(i == len(needle) - 1):
                        return index
        index += 1
    return  -1

def is_palindrome(x : str) -> bool :
    x = x.lower()
    x = re.sub(r'\W+', '', x)
    x = x.replace("_", "")
    front = 0
    if(len(x) == 0):
        return True
    rear = len(x) - 1
    is_palindrome = False
    while x[front] == x[rear]:
        if(front == rear):
            is_palindrome = True
            break
        if(len(x) % 2 == 0 and front + 1 == rear):
            is_palindrome = True
            break
        front += 1
        rear -=1
    return is_palindrome
 
def lengthOfLastWord(s: str) -> int: 
    result = re.findall(r"\w+", s)
    return len(result[-1])
    
def canJump(nums: List[int]) -> bool:
    ctr = 0
    while(ctr + nums[ctr] <= len(nums)):
            if(ctr + nums[ctr] == len(nums) - 1):
                return True
            if(len(nums) == 1):
                return True
            if(ctr + 1 > len(nums) -1):
                return True
            ctr +=1
    return False

def reverseWords(s: str) -> str:
    result = re.findall(r"\w+", s)
    last_index = len(result) - 1
    final_sentence = result[last_index]
    while(last_index > 0):
        last_index -= 1
        final_sentence += " " + result[last_index]
    return final_sentence

class SolutionRotateArray:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            for j in range(len(nums) - 1, 0, -1):
                self.swap(nums, j, j - 1)
                6
        print(nums)    
        
    def rotate2(self, nums: List[int], k: int) -> None: 
        mod = k % len(nums)  
        a = nums[:-mod]
        b = nums[-mod:]
        a.reverse()
        b.reverse()
        nums[:-mod] = a
        nums[-mod:] = b
        nums.reverse()
        print(nums)


def dailyTemperatures1(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if(temperatures[i] < temperatures[j]):
                result[i] = j - i
                break
    return result

def dailyTemperatures2(temperatures: List[int]) -> List[int]:
    stack = deque()
    result = [0]*len(temperatures)
    for i in range(len(temperatures)):
        while(stack and stack[-1][0] <  temperatures[i]):        
            poped = stack.pop()
            result[poped[1]] = i - poped[1]  
        stack.append([temperatures[i], i])
    return result

def dailyTemperaturesStack3(temperatures: List[int]) -> List[int]:
    stack = deque()
    result = [0]*len(temperatures)
    for i in range(len(temperatures)):
        while(stack and temperatures[stack[-1]] <  temperatures[i]):        
            poped = stack.pop()
            result[poped] = i - poped
        stack.append(i)
    return result



""" print(dailyTemperaturesStack3( [73,74,75,71,69,72,76,73]))


sol = SolutionRotateArray()
print(sol.rotate2([1,2,3,4,5,6,7], 10))

 """
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

def max_subarray_kadane(nums):
    """Find the largest sum of any contiguous subarray."""
    best_sum = nums[0]
    current_sum = 0
    for x in nums:
        if(current_sum < 0):
            current_sum = 0
        current_sum += x
        best_sum = max(best_sum, current_sum)
    return best_sum



def longestConsecutiveSequence(nums):
    hashset = {}
    max_sequence = 0
    for num in nums:
        hashset[num] = 1
        left_count = 0
        right_count = 0
        while(num - left_count - 1 in hashset):
            left_count += 1
        while(num + right_count + 1 in hashset):
            right_count += 1
        max_sequence = max(max_sequence, left_count + right_count + 1)
    return max_sequence

def longestConsecutiveSequence2(nums):
    hashset = set(nums)
    max_sequence = 0
    for num in nums:
        if(num - 1 not in hashset):
            longest = 0
            while(num + longest in hashset):
                longest +=1
        max_sequence = max(max_sequence, longest)
    return max_sequence



print(longestConsecutiveSequence2([100,4,200,1,3,2]))
""" print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([-2,-1,-2,-4])) """
#print(max_subarray_kadane([-2,1,-3,4,-1,2,1,-5,4]))
#print(max_subarray_kadane([-2,-1,-2,-4]))