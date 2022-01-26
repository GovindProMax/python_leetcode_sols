# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        myarr=[]
        def dfs (node,currsum):
            if not node: 
                return
            currsum+=node.val
            if (node.left == None) and (node.right == None):
                myarr.append(currsum==targetSum)
                #sumdict[h].append(node.val)
                #print("Looking at", node.val, "total vals:",currsum)  
            dfs(node.left,currsum)
            dfs(node.right,currsum)
            
        dfs (root,0)
        return True in myarr
        