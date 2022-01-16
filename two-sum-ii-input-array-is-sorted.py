class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap={}
        for i,n in enumerate(numbers):
            difference = target-n
            print(difference)
            if difference in prevMap:
                return [prevMap[difference],i+1]
            prevMap[n]=i+1