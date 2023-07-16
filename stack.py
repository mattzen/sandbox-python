import collections

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