class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [math.inf] * (amount+1)
        
        dp[0] = 0
        
        for leftover in range(1,amount+1):
            for coin in coins:
                
                if (leftover - coin) >= 0:
                    dp[leftover] = min(dp[leftover], 1 + dp[leftover - coin])
        
        if dp[amount] == math.inf: return -1 
        else: return dp[amount]
                