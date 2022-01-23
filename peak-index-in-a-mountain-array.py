### O(n) Soln ###
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        for i in range(0,len(arr)-1):
            if arr[i+1] < arr[i]:
                return i

### O (log N) Soln ###
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        right = len(arr) - 1
        
        middle = (right + left) // 2
        
        while left < right:
            if (arr[middle-1] > arr[middle]) and (arr[middle] > arr[middle+1]):
                    right = middle
                    middle = (right + left) // 2
            elif (arr[middle-1] < arr[middle]) and (arr[middle] < arr[middle+1]):
                    left = middle
                    middle = (right + left) // 2
            else:
                return middle