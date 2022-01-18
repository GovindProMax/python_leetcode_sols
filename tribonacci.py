class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        
        if n == 0:
            return 0
        if n == 1:
            return second
        if n == 2:
            return third
        for i in range(3,n+1):
            
            my_num = first + second + third
            first = second
            second = third
            
            third = my_num            
        
        return my_num
 ### Alternate ###
 class Solution:
    myTable = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        if n in self.myTable:
            return self.myTable[n]

        self.myTable[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        return self.myTable[n]
        