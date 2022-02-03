class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        counter = 0
        mystr=""
        for i in range(len(s)-1,-1,-1):
            if (s[i] != '-') and (counter == k-1):
                mystr = '-' + s[i].upper() + mystr 
                counter = 0 
            elif (s[i] != '-'):
                mystr=s[i].upper() + mystr
                counter+=1
        if mystr and mystr[0] =="-":
            return mystr[1:]
        return mystr
        
        
            
        