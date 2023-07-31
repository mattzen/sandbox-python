from collections import deque
import heapq
from typing import *





class SolutionHeaps:
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
        
    
    
    def recalculateDown(self, nums):
        index = 0
        while (2*index + 1 < len(nums)):
            smallerIndex = 2* index + 1
            if (2*index + 2 < len(nums) and nums[2*index + 1] < nums[2*index + 2]):
            
                smallerIndex = 2*index + 2
            if (nums[smallerIndex] >= nums[index]):
                break
        
            nums[smallerIndex], nums[index] = nums[index], nums[smallerIndex]
 
    def findKthLargest(self, nums: List[int], k: int) -> int:
          # Index of last non-leaf node
        self.buildHeap(nums)
        

        for i in range(k-1):
            nums.pop(0)
            self.heapify(self, nums, len(nums), 0)
             
        return nums[0]
                 
    def buildHeap(self, nums):
        n= len(nums)
        startIdx = n // 2 - 1
    
        # Perform reverse level order traversal
        # from last non-leaf node and heapify
        # each node
        for i in range(startIdx, -1, -1):
            self.heapify(nums, n, i)
               
    def heapify(self, arr, N, i):
    
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
    
        # If left child is larger than root
        if l < N and arr[l] > arr[largest]:
            largest = l
    
        # If right child is larger than largest so far
        if r < N and arr[r] > arr[largest]:
            largest = r
    
        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
    
            # Recursively heapify the affected sub-tree
            self.heapify(arr, N, largest)
        
    


sol  = SolutionHeaps()
print(sol.findKthLargest2([3,2,3,1,2,4,5,5,6], 4))