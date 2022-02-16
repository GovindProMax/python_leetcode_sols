class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        finalSet=[]
        
        def backtracking(i, temp, total):
            if total == target:
                finalSet.append(temp.copy())
                return
            if i >= len(candidates) or total > target:
                return
            temp.append(candidates[i])
            backtracking(i, temp, total + candidates[i])
            temp.pop()
            backtracking(i + 1, temp, total)
            
        backtracking(0,[],0)
        
        return finalSet
            
            
                
            
            
        