class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newarr=[]
        for index in range(0,len(nums)):
            newarr.append(nums[nums[index]])
        return newarr