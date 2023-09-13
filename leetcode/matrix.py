import math
from typing import List

class SolutionMatrixRotate90:
    
    def swap(self, matrix, i, j, k, l):
        temp = matrix[i][j]
        matrix[i][j] = matrix[k][l]
        matrix[k][l] = temp
        
    def rotate_90(self, matrix: List[List[int]]) -> None:
        ctr = 0
        dim = len(matrix) - 1
        #for level in range(math.floor(len(matrix)/2)):
        while(ctr < dim):
            for index in range(dim - ctr):
                self.swap(matrix, ctr, ctr + index, dim - index, ctr)
                self.swap(matrix, dim - index, ctr, dim, dim - index)  
                self.swap(matrix, dim, dim - index, ctr + index, dim) 
            ctr += 1
            dim -= 1
       
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#matrix = [[1,2],[3,4]]

print(matrix)
sol = SolutionMatrixRotate90()
sol.rotate_90(matrix)
print(matrix)