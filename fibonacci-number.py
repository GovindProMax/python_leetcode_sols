class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        
        if n<2:
            return n
        for i in range(2,n+1):
            my_num = first + second
            
            
            first = second
            second = my_num            
        
        return my_num