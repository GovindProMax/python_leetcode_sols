class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        
        if n < 3:
            return n

        for i in range(3, n+1):
            current = first + second
            first = second
            second = current
        
        return current