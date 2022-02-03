import re
class Solution:
    def isPalindrome(self, s: str) -> bool:  
        new=re.sub('[^A-Za-z0-9]+','', s).lower()
        return new == new[::-1]