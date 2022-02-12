class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for n in range(len(nums)-1,-1,-1):
            for j in range(n+1,len(nums)):
                if nums[n] < nums[j]:
                    dp[n] = max(dp[n], 1 + dp[j])
            
        return max(dp)