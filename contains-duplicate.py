class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict={}
        
        for n in nums:
            if n in mydict:
                return True
            else:
                mydict[n] = 0
                
        return False


### Using Sets ###
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)
        if len(nums) == len(set1):
            return False
        return True