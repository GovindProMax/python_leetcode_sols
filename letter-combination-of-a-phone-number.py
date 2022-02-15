class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        phoneDict={"2":"abc",
                  "3":"def",
                  "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz"}
        
        finalList=[]
        
        def backtracking(i, s):
            if len(s) == len(digits):
                finalList.append(s)
                return
            
            for n in phoneDict[digits[i]]:
                backtracking(i+1,s+n)
        
        backtracking(0,"")
        
        return finalList
            
            
        