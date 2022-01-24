# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        sumdict=defaultdict(list)
        if root == None: 
            return 0
        
        def dfs (node, h):
            if not node: 
                return
            if (node.left == None) and (node.right == None):
                sumdict[h].append(node.val)
            dfs(node.left,h+1)
            dfs(node.right,h+1)
        dfs (root,0)
        return (max(sumdict) + 1)
        
        