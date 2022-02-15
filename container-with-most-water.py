class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        left=0
        right=len(nums) - 1
        maxArea=0
        
        while left < right:
            
            area= (right-left) * min(nums[left],nums[right])
            #print("left is",left,"right is ", right, "area is",area)
            
            maxArea= max(maxArea,area)
            
            if nums[left]<nums[right]:
                left+=1
            else:
                right-=1
        return maxArea