import math

class SolutionMajorityElement:
    def majorityElement1(nums):
        result = {} 
        for element in nums: 
            if element in result:
                result[element] = result[element] + 1
            else:
                result[element] =  1        
        maximum = max(result.values())
        index = 0
        for v in result.keys():
            if(result[v] == maximum):
                index = v
        return index
    
    def majorityElement2(nums):
        result = {} 
        current_max = 0
        last_max = 0
        max_element = nums[0]
        for element in nums: 
            if element in result:
                result[element] = result[element] + 1
                current_max = result[element]
                if(last_max <= current_max):
                    last_max = current_max
                    max_element = element
            else:
                result[element] =  1    
        return max_element   
     
    def majorityElement3(nums):
        nums.sort()
        return nums[math.ceil(len(nums)/2)] 
    
    def majorityElement4(nums):
        nums.sort()
        return nums[math.floor(len(nums)/2)]
    