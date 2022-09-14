class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHashMap = {}
        
        bucketSortList = [[] for x in range(0,len(nums)+1)]
        
        for x in nums:
            if x in countHashMap:
                countHashMap[x] = 1 + countHashMap[x]
            else:
                countHashMap[x] = 1
        
        for index,value in countHashMap.items():
            bucketSortList[value].append(index)
        
        res = []
        
        for i in range(len(bucketSortList)-1,0,-1):
            for x in bucketSortList[i]:
                res.append(x)
                if len(res) == k:
                    return res