from typing import *


class SolutionIntervals:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            begin = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            end = nums[i]
            if begin == end:
                ans.append(str(begin))
            else:
                ans.append(str(begin) + "->" + str(end))
            i += 1
        return ans
    
    
    


sol = SolutionIntervals()
print(sol.summaryRanges([0,1,2,4,5,7]))