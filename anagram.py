class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for char in s:
            if char in d.keys():
                d[char] = d[char]+1
            else:
                d[char] = 1
        
        for char in t:
            if char in d.keys():
                d[char]=d[char]-1
            else:
                return False
        print(d)
        
        return all(x == 0 for x in d.values())