from collections import deque
from typing import *


class SolutionMonotonicStack:

    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if(temperatures[i] < temperatures[j]):
                    result[i] = j - i
                    break
        return result

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while(stack and stack[-1][0] <  temperatures[i]):        
                poped = stack.pop()
                result[poped[1]] = i - poped[1]  
            stack.append([temperatures[i], i])
        return result

    def dailyTemperaturesStack3(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while(stack and temperatures[stack[-1]] <  temperatures[i]):        
                poped = stack.pop()
                result[poped] = i - poped
            stack.append(i)
        return result

sol = SolutionMonotonicStack()
print(sol.dailyTemperaturesStack3( [73,74,75,71,69,72,76,73]))
