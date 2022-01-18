class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = [str(n) for n in str(x)]
        
        if len(res) == 1:
            return True   
        while len(res) > 1 :
            if res[0] == res[-1]:
                res.pop(0)
                res.pop(-1)
            else:
                return False
        
        if len(res) <= 1:
            return True
        
        return False


### Alternate ###
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]