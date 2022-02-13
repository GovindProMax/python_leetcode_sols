class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Initial pointers
        low=0
        high=len(nums) - 1
        mid= (high+low) // 2
        
        ## Check if target is in which pivoted half and set pointers accordingly
        if (nums[low] <= nums[mid]) and (nums[mid] > nums[high]):
            rightOfIncreasing= nums.index(max(nums[mid:]))
            if (target >= nums[low]) and (target<=nums[rightOfIncreasing]):
                high = rightOfIncreasing
            else:
                low = rightOfIncreasing +1
        ## Check if target is in which pivoted half and set pointers accordingly    
        elif (nums[mid] <= nums[high]) and (nums[mid] < nums[low]):
            leftOfIncreasing= nums.index(min(nums[:mid+1]))
            if (target <= nums[high]) and (target>=nums[leftOfIncreasing]):
                low = leftOfIncreasing
            else:
                high = leftOfIncreasing - 1
                
        ## Simple binary search     
        mid = (high+low) // 2
        while low <= high:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
                mid = (high+low) // 2
            elif nums[mid] > target:
                high = mid - 1
                mid = (high+low) // 2
        return -1