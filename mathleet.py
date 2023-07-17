class SolutionMath:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i < x:
            i = i + 1
        return i-1
    
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if(n > 0):
            for i in range(n):
                result = result * x 
        else:
            for i in range(-n):
                result = result * 1/x
        return result


s = SolutionMath()
print(s.myPow(0.00001,2147483647))