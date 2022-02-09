## brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        originalLength=len(s)
        counter=0
        maxLen=0
        if s[::1] == s[::-1]: return s
        
        while counter < originalLength:
            length=len(s)
            while 0 < length:
                #print("checking",s[:length], "with", s[length-1::-1])
                if (s[:length] == s[length-1::-1]):
                    temp=len(s[:length])
                    if maxLen < temp:
                        finalString=s[:length]
                        maxLen=temp
                    length-=1
                else:
                    length-=1
            s=s[1:]
            if len(finalString) > len(s):
                return finalString
            #print("after slice",s)
            
            counter+=1
        return finalString
        #longest_string = max(maxPalindrome, key=len)
        #print(longest_string)
        #return longest_string