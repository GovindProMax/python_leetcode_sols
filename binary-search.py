class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        middle = (start + end) // 2
        
        while start <= end:
            if target == nums[int(middle)]:
                return int(middle)
            elif target < nums[int(middle)] :
                end = middle-1
                middle = (start + end) // 2
            elif target > nums[int(middle)] :
                start = middle+1
                middle = (start + end) // 2
        
        return -1