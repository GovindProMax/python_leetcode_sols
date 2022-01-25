class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        newarr = []
        
        while left<=right:
            if abs(nums[left]) < abs(nums[right]):
                newarr.insert(0,nums[right] ** 2)
                right = right - 1
            else:
                newarr.insert(0,nums[left] ** 2)
                left = left + 1
        
        return newarr
                