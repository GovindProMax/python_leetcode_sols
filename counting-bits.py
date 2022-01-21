class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0] * (n+1)
        
        offset = 1
        
        for index in range(1, n+1):
            if offset * 2 == index:
                offset = index
            
            dp[index] = 1 + dp[index-offset]
            
        return dp