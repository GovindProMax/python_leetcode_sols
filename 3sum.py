class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        array.sort()
        triplets=[]
        

        for index in range(len(array)-2):
            left=index+1
            right=len(array)-1
            if index >0 and array[index-1]==array[index]:
                continue
            while left<right:
                currentSum=array[index]+array[left]+array[right]
                if currentSum==0:
                    triplets.append([array[index],array[left],array[right]])
                    left+=1
                    right-=1
                    # skip the repetition of the same element
                    while left < right and ( array[left] == array[left-1] ):
                        left += 1
                    # skip the repetition of the same element
                    while left < right and ( array[right] == array[right+1] ):
                        right -= 1
                elif currentSum<0:
                    left+=1
                elif currentSum>0:
                    right-=1
        return triplets