class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        res=''
        
        for x in range(0,len(prefix)):
            for mystr in strs:
                if len(res) == len(mystr) or mystr[x] != prefix[x]:
                    return res
            res+=prefix[x]
        return res