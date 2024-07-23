import collections
from typing import List

class SolutionNumOfIslands:
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [0, 1, 0, -1, 0]

        def bfs(r, c):
            q = collections.deque([(r, c)])
            grid[r][c] = '2'  # Mark '2' as visited
            while q:
                i, j = q.popleft()
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if grid[x][y] != '1':
                        continue
                    q.append((x, y))
                    grid[x][y] = '2'  # Mark '2' as visited

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1

        return ans
        
      
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                return
            if grid[i][j] != '1':
                return

            grid[i][j] = '2'  # Mark '2' as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1

        return ans
    
    
    def numIslandsBFSMy(self, grid: List[List[str]]) -> int: 
        m = len(grid)
        n = len(grid[0])
        queue = collections.dequeue(grid[0][0])
        
        while(queue):
            for i in range(m-1):
                for j in range(n-1):
                    curr_el = queue.popleft()
                    if(grid[i, j]== 1):
                        grid[i, j] = 2
                    queue.append(grid[m + 1, n])
                    queue.append(grid[m, n + 1])


    def countIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        len_row = len(grid)
        len_column = len(grid[0])
        
        
        def dfs(row, column):
            if(row >= len_row or column >= len_column or row < 0 or column < 0):
                return
            if(grid[row][column] == "0" or grid[row][column] == "-1" ):
                return
            grid[row][column] = "-1"
            for dir in directions:
                dfs(row + dir[0], column + dir[1])
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    dfs(i, j)
                    islands_count += 1
        return islands_count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = SolutionNumOfIslands()
print(sol.countIslands(grid))
#print(sol.numIslandsBFS(grid))

