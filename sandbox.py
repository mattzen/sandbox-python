from two_sum import *
from other_problems import *
from majority_element import *
from typing import List
import re

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def sliding_window(elements, window_size):   
    if len(elements) <= window_size:
       return elements
    for i in range(len(elements)):
        print(elements[i:i+window_size])  

class SolutionHIndex:
    def hIndexSort(self, citations: List[int]) -> int:
        citations.sort()
        l = len(citations)
        for i in range(l):
            if(citations[i] >= l - i):
                 return l - i
        return 0
  
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        accumulate = 0
        count = [0] * (n + 1)

        for citation in citations:
            count[min(citation, n)] += 1

        # To find the largeset h-index, loop from back to front
        # I is the candidate h-index
        for i, c in reversed(list(enumerate(count))):
            accumulate += c
            if accumulate >= i:
                return i
     


if __name__ == "__main__":
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
    sol = SolutionHIndex()
    print(sol.hIndex([1,3,1]))