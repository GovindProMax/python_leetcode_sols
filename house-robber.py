class Solution:
    def rob(self, nums: List[int]) -> int:
        firstrob=0
        secondrob=0
        
        for money in nums:
            temp=max(money+firstrob,secondrob)
            firstrob=secondrob
            secondrob=temp
        return secondrob
##### Alternate ######
## found at https://leetcode.com/problems/house-robber/discuss/846235/Python-Simple-Solution-Explained-(video-%2B-code
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for x in range(2, len(nums)):
            dp[x] = max(dp[x - 1], nums[x] + dp[x - 2])
        
        return dp[-1]