class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def gen_permutatons(nums, perm, perms):
            if not nums:
                perms.append(perm[:])
                return
            
            for i, n in enumerate(nums):
                perm.append(n)
                gen_permutatons(nums[:i] + nums[i+1:], perm, perms)
                perm.pop()
        perms = []
        gen_permutatons(nums, [], perms)
        return perms


### Alternate ###

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            def backtrack(path):
                if len(path) == n:
                    res.append(path)
                else:
                    for i in range(n):
                        if i not in visited:
                            visited.add(i)
                            backtrack(path + [nums[i]])
                            visited.remove(i)
            res, visited, n = [], set(), len(nums)
            backtrack([])
            return res


### Alternate ###

class Solution:
    def __init__(self):
        self.res=[]
        
    def permute(self, nums):
        
        self.backtracking(nums, [])
        
        return self.res
    
    def backtracking(self,nums,path):
        
        if not nums:
            self.res.append(path)   
        for n in range(len(nums)):
            self.backtracking(nums[:n]+nums[n+1:],path+[nums[n]])