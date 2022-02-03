class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        mid = (start + end) // 2
        
        while start <= end:
            if target == nums[int(mid)]:
                return int(mid)
            elif target < nums[int(mid)] :
                end = mid-1
                mid = (start + end) // 2
            elif target > nums[int(mid)] :
                start = mid+1
                mid = (start + end) // 2

        return mid +1        
