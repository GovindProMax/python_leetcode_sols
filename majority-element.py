class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict={}
        
        for n in nums:
            if n in mydict:
                mydict[n]=mydict[n] + 1
            else:
                mydict[n]=1
        return list(mydict.keys())[list(mydict.values()).index(max(mydict.values()))]
