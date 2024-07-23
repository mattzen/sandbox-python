from collections import deque
import heapq
from typing import *
class SolutionHeaps:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
        
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

class SolutionQuickSelect:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        def quickSelect(l: int, r: int, k: int) -> int:
            pivot = nums[r]

            nextSwapped = l
            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[nextSwapped], nums[i] = nums[i], nums[nextSwapped]
                    nextSwapped += 1
            nums[nextSwapped], nums[r] = nums[r], nums[nextSwapped]

            count = nextSwapped - l + 1  # Number of nums >= pivot
            if count == k:
                return nums[nextSwapped]
            if count > k:
                return quickSelect(l, nextSwapped - 1, k)
            return quickSelect(nextSwapped + 1, r, k - count)

        return quickSelect(0, len(nums) - 1, k)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest2(self, nums: List[int], k: int) -> int:
            k = len(nums) - k
            left, right = 0, len(nums) - 1

            while left < right:
                pivot = self.partition(nums, left, right)

                if pivot < k:
                    left = pivot + 1
                elif pivot > k:
                    right = pivot - 1
                else:
                    break

            return nums[k]
        
    def findKthLargest3(self, nums: List[int], k: int) -> int:
            k = len(nums) - k
            left, right = 0, len(nums) - 1

            while left < right:
                pivot = self.partition(nums, left, right)

                if pivot < k:
                    left = pivot + 1
                elif pivot > k:
                    right = pivot - 1
                else:
                    break

            return nums[k]


sol  = SolutionQuickSelect()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))


#sol  = SolutionHeaps()
#print(sol.findKthLargest2([3,2,3,1,2,4,5,5,6], 4))