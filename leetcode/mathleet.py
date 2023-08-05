class SolutionMath:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i < x:
            i = i + 1
        return i-1
    
    def myPow(self, x: float, n: int) -> float:
        return 0


s = SolutionMath()
print(s.myPow(0.00001,2147483647))