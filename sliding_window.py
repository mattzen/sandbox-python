from typing import List
    
class SolutionMinSubArray:
        def minSubArrayLen(self, nums, s):
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
                
                
            
    
sol = SolutionMinSubArray()
print(sol.minSubArrayLen([2,3,1,2,4,3], 7))