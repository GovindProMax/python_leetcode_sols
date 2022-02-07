class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while (i < (len(nums))):
            while i!=len(nums) and (nums[i]==val):
                nums.pop(i)
            i+=1