# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Copied from LEETCODE ### I will upload my solution soon
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(curr, target, root):
            if not root.left and not root.right and target - root.val == 0:
                res.append(curr + [root.val])
            if root.left:
                dfs(curr + [root.val], target-root.val, root.left)
            if root.right:
                dfs(curr + [root.val], target-root.val, root.right)
    
        if not root: return []
        dfs([], targetSum, root)
        return res