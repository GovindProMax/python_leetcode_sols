class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict={}
        for i,n in enumerate(nums):
            if n in myDict:
                if abs(myDict[n] - i) <= k:
                    return True
                else:
                    myDict[n] = i
            else:
                myDict[n] = i
        return False