class Solution:
    def moveZeroes(self, array: List[int]) -> None:
        left=0
        right=0
        while right<len(array):
            if array[right] != 0: 
                print('swapping',array[left],'and',array[right])
                array[left],array[right]=array[right],array[left]
                left+=1
            right+=1
        return array


            