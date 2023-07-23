import collections
from typing import List
import sys

def SumOfDigits(num : int) -> int:
    num = str(num)
    if len(num) == 1:
        return int(num)
    return int(num[0]) + SumOfDigits(int(num[1:]))
    
def SumofDigitsIterative(num : int) -> int:
    holder = 0
    strNum = str(num)
    for element in strNum:
        holder += int(element)
    return holder

 #ex 23   

def phoneNumbers(digits):
    d = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pgrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
    
    result = []
    def backtrack(index, curStr):
        if(len(curStr) == len(digits)):
            result.append(curStr)
            return
        for i in d[digits[index]]:
            backtrack(index + 1, curStr + i)
            
    if(digits):
        backtrack(0, "")
    return result
  
class SolutionCombinations:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #[1,n] 
        #[1..len(k)]    
        result = []
        
        def backtrack(current_set, ctr):
            if(len(current_set) == k):
                result.append(current_set.copy())
                return
            for i in range(ctr,n+1):
                current_set.append(i)
                backtrack(current_set, i+1)
                current_set.pop()
            
        backtrack([], 1)   
        return result
       
class SolutionStairs:         
    def climbStairsDP(self, n): 
        lookup = {}
        def recursiveStairs(n, index):
            if(index in lookup.keys()):
                return lookup[index]
            if(index == n): 
                return 1
            if(index > n):
                return 0
            for i in range (n):
                lookup[index] = recursiveStairs(n, index + 1) + recursiveStairs(n, index + 5)
                return lookup[index]
        return recursiveStairs(n, 0)
    
    def climbStairs(self, n): 
        def recursiveStairs(n, index):
            if(index == n): 
                return 1
            if(index > n):
                return 0
            for i in range (n):
                return recursiveStairs(n, index + 1) + recursiveStairs(n, index + 2)
        return recursiveStairs(n, 0)
    
    def climbStairsIT(self, n: int) -> int:
        prev1 = 1  # dp[i - 1]
        prev2 = 1  # dp[i - 2]

        for _ in range(2, n + 1):
            dp = prev1 + prev2
            prev2 = prev1
            prev1 = dp

        return prev1
            
def permute(nums: List[int]) -> List[List[int]]:
    result = []
    
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def permute_helper(nums, index):
        if(index == len(nums)):
            result.append(nums.copy())
            return
        for i in range(index, len(nums)):
                swap(nums, i, index)
                permute_helper(nums, index + 1)
                swap(nums, i, index)
    
    
    permute_helper(nums, 0)
    
    return result            
        

def minPathSumBottomUp(grid: List[List[int]]) -> int:
    
    row_len = len(grid[0])
    col_len = len(grid)
        
    def dfs(grid, i, j):
        #last element bottom left corner
        if(i == col_len - 1 and j == row_len -1):
            return grid[i][j]  
        elif(i >= col_len or j >= row_len):
            return sys.maxsize
        else:
            return grid[i][j] + min(dfs(grid, i + 1, j),
                                    dfs(grid, i, j + 1))
            
                
    return dfs(grid, 0, 0)
    
def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
      for j in range(n):
        if i > 0 and j > 0:
          grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        elif i > 0:
          grid[i][0] += grid[i - 1][0]
        elif j > 0:
          grid[0][j] += grid[0][j - 1]

    return grid[m - 1][n - 1]   
    

def minPathSumBottomUpDP(grid: List[List[int]]) -> int:
    
    row_len = len(grid[0])
    col_len = len(grid)
    dp_cost = [] * row_len
    
    print(dp_cost)
    
    def dfs(grid, i, j):
        #last element bottom left corner
        if(i == col_len - 1 and j == row_len -1):
            return grid[i][j]  
        elif(i >= col_len or j >= row_len):
            return sys.maxsize
        else:
            if(not dp_cost or not dp_cost[i][j]):
                dp_cost.appendgrid[i][j] + min(dfs(grid, i + 1, j),
                                                dfs(grid, i, j + 1))
                return
            else:
                return dp_cost[i][j]
            
                
    return dfs(grid, 0, 0)

def minPathSumTopDown(grid: List[List[int]]) -> int:
    def minCost(cost, m, n):
        if (n < 0 or m < 0):
            return sys.maxsize
        elif (m == 0 and n == 0):
            return cost[m][n]
        else:
            return cost[m][n] + min(minCost(cost, m-1, n),
                                    minCost(cost, m, n-1))
    return minCost(grid, len(grid)-1, len(grid[0])-1)
        

print(minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
                            [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
                            [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
                            [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
                            [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
                            [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
                            [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
                            [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
                            [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
                            [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
                            [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
                            [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]])) 

#print(minPathSumBottomUp([[1, 3, 1],[1, 5, 1],[4, 2, 1]])) 
#print(minPathSumBottomUp([[1, 2, 3],[4, 5, 6]])) 

#print(minPathSumTopDown([[1, 2, 3],[4, 5, 6]]))     

print(minPathSum([[1, 3, 1],[1, 5, 1],[4, 2, 1]] ))    
    
#sol = SolutionStairs()
#print(sol.climbStairsDP(40))
#print(sol.climbStairsIT(40))
#print(permute([1,2,3]))
