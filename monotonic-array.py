class Solution:
    def isMonotonic(self, array: List[int]) -> bool:
        pointer=0
        if len(array)<2: return True
        if array[0]<=array[len(array)-1]:
            while pointer < len(array)-1:
                if array[pointer]>array[pointer+1]:
                    return False
                pointer+=1
        elif array[0]>array[len(array)-1]:
            while pointer < len(array)-1:
                if array[pointer]<array[pointer+1]:
                    return False
                pointer+=1
        return True