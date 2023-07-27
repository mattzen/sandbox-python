import collections
import math
from typing import List

class SolutionRemoveStars:
    def removeStars1(self, s: str) -> str:
        result = ""
        stack = collections.deque()
        for char in s:
            if(char != "*"):
                stack.append(char)
            else:
                stack.pop()
        while(stack):
            result += stack.popleft()
        return result
    
    def removeStars2(self, s: str) -> str:
        result = ""
        for char in s:
            if(char != "*"):
                result += char
            else:
                result = result[:len(result)-1]
        return result
    
    def removeStars3(self, s: str) -> str:
        stack = collections.deque()
        for char in s:
            if(char != "*"):
                stack.append(char)
            else:
                stack.pop()
            
        return "".join(stack)

class SolutionAsteroids:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        return []
            
        
        
        
        
sol = SolutionAsteroids()
#print(sol.asteroidCollision([-2,-2,1,-2]))       
print(sol.asteroidCollision([5,10,-5]))       
""" sol = SolutionRemoveStars()
print(sol.removeStars3("leet**cod*e")) """