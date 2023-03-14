class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedSquares=[0 for num in nums]
        left=0
        right=len(nums)-1
        pointer=len(nums)-1

        while left<=right:
            if abs(nums[left])<=abs(nums[right]):
                sortedSquares[pointer]=nums[right]*nums[right]
                right-=1
                pointer-=1
            else:
                sortedSquares[pointer]=nums[left]*nums[left]
                left+=1
                pointer-=1
        
        return sortedSquares