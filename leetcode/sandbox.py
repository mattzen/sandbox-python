from linked_list import SolutionHIndex
from two_sum import *
from other_problems import *
from majority_element import *
from typing import List
import re
import functools

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def sliding_window(elements, window_size):   
    if len(elements) <= window_size:
       return elements
    for i in range(len(elements)):
        print(elements[i:i+window_size])  


def ReturnNonDuplicate(nums):
    return functools.reduce(lambda x,y: x^y, nums)


def valueTypeVsReferenceType():
    arr = [1,2,3,4]
    arr2 = arr
    #modifies arr2
    arr.append(5)

    a = 2
    b = a
    #doesnt modify a
    b = 4

    print(a, b, arr2)


def SumOfDigits(n):
    if n == 0:
        return 0
    return n%10 + SumOfDigits(n//10)

def SumofDigitsIterative(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

def is_palindrome(s):
    s = re.sub('[^a-zA-Z0-9]', '', s)
    s = s.lower()
    return s == s[::-1]

def lengthOfLastWord(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    return len(s.split()[-1])

def reverseWords(s):
    s = s.strip()
    if len(s) == 0:
        return ""
    return " ".join(s.split()[::-1])
    
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1 
        


if __name__ == "__main__":
    print(ReturnNonDuplicate([1,3,2,2,1]))
    #print(SumOfDigits(123456767))
    #print(SumofDigitsIterative(123456767))
    #print(Solution.majorityElement3([1,3,2,2,2,2]))
    #sol = Solution()
    #print(sol.removeElement2([3,2,2,3], 3))
    #print(is_palindrome("aSmanaplanacanalpanama"))
    #print(is_palindrome("A man, a plan, a canal: Panama"))
    #print(is_palindrome("ab_a"))
    #print(lengthOfLastWord("   fly me   to   the moon  "))
    #print(reverseWords("the sky is blue"))
    #print(strStr("leetcode", "leeto"))
    #print(strStr("sdbutsad", "sad"))
    #sliding_window([1,2,3,4,5,6,7,8], 3)
    #d = Dog("Kensai", 10)
    #print(d.breed)
    #print(minSubArrayLen([2,3,1,2,4,3], 7))
    #print(phoneNumbers("2345"))
    #print(twoSumHashTable([1,2,3,4,55,7], 8))
    #sol = SolutionHIndex()
    #print(sol.hIndex([1,10,1]))