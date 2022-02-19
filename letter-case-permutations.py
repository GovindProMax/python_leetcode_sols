class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        finalList=[]
        path=[]
        def dfs(i): 
            if i >= len(s):
                print(path)
                finalList.append("".join(path))
                return
            if s[i].isalpha():
                path.append(s[i].upper())
                dfs(i+1)
                path.pop()
                path.append(s[i].lower())
                dfs(i+1)
                path.pop()
            else:
                path.append(s[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return finalList
                    
                
                    
        