from typing import List

def minSubArrayLen1(nums, s):
        head, rear, current_total, min_length = 0 , 0 , 0, len(nums) + 1
        while rear < len(nums):
            current_total += nums[rear]
            rear += 1
            while current_total >= s:
                min_length = min(min_length, rear - head)
                current_total -= nums[head]
                head += 1
        return min_length if min_length != len(nums) + 1 else 0
    
def minSubArrayLen2(nums, s):
        l = 0
        total = 0
        min_lenght = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while(total >= s):
                min_lenght = min(min_lenght, r - l + 1)
                total -= nums[l]
                l += 1
            
        return min_lenght if min_lenght != float("inf") else 0
            
            
            
    

print(minSubArrayLen2([2,3,1,2,4,3], 7))