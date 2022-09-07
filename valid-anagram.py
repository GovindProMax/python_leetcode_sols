#1 Solution: Used Counter(string) to compare both words
#2 Solution: Actually implemented hashmap and then compared the two

class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        return self.mycounter(s) == self.mycounter(t)
        
    def mycounter(self, mystr: str) -> dict:
        c = {}
        for x in mystr:
            if x in c:
                c[x] = 1 + c[x]
            else:
                c[x] = 1
        return c