class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finalPost = len(nums)-1
        for n in range(len(nums)-1,-1,-1):
            if n + nums[n] >= finalPost:
                finalPost=n
            
        return finalPost==0