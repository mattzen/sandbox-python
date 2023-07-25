import collections
import math
from typing import List

class SolutionStack:
    def isValidParenthesis(self, s: str) -> bool:
        closing = [")","]","}"]
        opening = ["(","[","{"]
        if(not s):
            return True
        if(len(s) == 1):
            return False
        stac = collections.deque(s[0])
        i = 1
        for i in range(len(s)):
            while(stac):
                if(s[i] == ")" or s[i] == "]" or s[i] == ""):
                    return False
        return True
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

    
6

class SolutionAsteroids:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = collections.deque()
        for asteroid in asteroids:  
            if(stack):
                if(stack and asteroid < 0 and stack[-1] > 0):
                    while(stack and asteroid < 0 and stack[-1] > 0):
                        if(stack and abs(asteroid) > abs(stack[-1])):
                            stack.pop
                            stack.append(asteroid)
                        elif(stack and abs(asteroid) == abs(stack[-1])):
                            stack.pop()
                        else:
                            break 
                else:
                   stack.append(asteroid)      
            else:
                stack.append(asteroid)    

        return list(collections.deque(stack))
            
        
        
        
        
sol = SolutionAsteroids()
#print(sol.asteroidCollision([-2,-2,1,-2]))       
print(sol.asteroidCollision([5,10,-5]))       
""" sol = SolutionRemoveStars()
print(sol.removeStars3("leet**cod*e")) """