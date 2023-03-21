class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int,{0:1})

        currSum=0
        res = 0

        for num in nums:
            currSum+=num
            diff = currSum-k
            if diff in prefix:
                res+=prefix[diff]
                prefix[currSum]+=1
            else:
                prefix[currSum]+=1
        return res