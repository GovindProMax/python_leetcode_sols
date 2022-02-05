class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        mydict={}
        for elem in nums:
            if elem in mydict:
                return elem
            else:
                mydict[elem] = 0