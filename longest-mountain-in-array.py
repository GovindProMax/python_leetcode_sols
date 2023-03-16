class Solution:
    def longestMountain(self, array: List[int]) -> int:
        i = 1
        length = len(array)
        maximum = 0
        while(i<length):
            count=1
            if(array[i-1]>=array[i]):
                i+=1
                continue
            while(i<length and array[i-1]<array[i]):
                i+=1
                count+=1
            if(i>=length or array[i-1] == array[i]):
                continue
            while(i<length and array[i-1]>array[i]):
                i+=1
                count+=1
            maximum = max(maximum,count)
        return maximum