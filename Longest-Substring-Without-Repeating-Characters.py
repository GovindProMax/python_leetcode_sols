class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        mydict={}
        maxlen=0
        length=0
        for i,char in enumerate(s):
            if char in mydict:
                maxlen=max(maxlen,length)
                mydict.clear()
                increment=1
                tempVar=s[i-increment]
                while char != tempVar:
                    mydict[tempVar]=0
                    tempVar=s[i-increment]
                    increment+=1
                mydict[char]=0
                length=len(mydict)
                    
            else:
                mydict[char]=0
                length+=1
        maxlen=max(maxlen,length)
        return maxlen