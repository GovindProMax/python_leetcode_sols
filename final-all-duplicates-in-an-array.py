class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mydict={}
        finallist=[]
        for elem in nums:
            if elem in mydict:
                finallist.append(elem)
            else:
                mydict[elem] = 0
        return set(finallist)