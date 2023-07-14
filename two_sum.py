from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
     current_sum = 0
     for i in range(0, len(nums)):
         current_sum = nums[i]
         for j in range(i+1, len(nums)):
             if(current_sum + nums[j] == target):
                 return i, j
             
def twoSumHashTable(nums: List[int], target: int) -> List[int]:
    table = dict() 
    for i in range(0, len(nums)):
        index = target - nums[i]
        if(index in table.keys()):
            return i, table[index]
        table[nums[i]] = i
