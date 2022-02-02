class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp=0
        
        ## Remove trailing spaces
        while s[-1:len(s)] == ' ':
            s = s[:-1]
        
        ## Get length of last word and store it in temp variable
        while s[-1: len(s)] != ' ' and len(s)!=0:
            temp+=1
            s = s[:-1]
        return temp
        