class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        """dict = {}
        for index in range(len(array)):
            if array[index] in dict:
                return array[index]
            else:
                dict[array[index]] = False
        return -1*/
        
        Floyd's algorithm:
        """
        
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