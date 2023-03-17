class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        """
        O(n) space solution
        dict = {}
        for index in range(len(array)):
            if array[index] in dict:
                return array[index]
            else:
                dict[array[index]] = False
        return -1*/
        
        Floyd's algorithm:
        O(1) space solution without modifying array
        
        
        slow,fast=0,0

        while True:
            slow=array[slow]
            fast=array[array[fast]]
            if slow==fast:
                break
        slow2=0

        while True:
            slow=array[slow]
            slow2=array[slow2]
            if slow==slow2:
                return slow
                
        When you can modify the array:
        """
    def findDuplicate(self, array: List[int]) -> int:
        for value in array:
            absVal = abs(value)

            if array[absVal-1]<0:
                return absVal
            array[absVal-1]*=-1
        return -1
