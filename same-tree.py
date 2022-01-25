# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True
        if q is None or p is None:
            return False
        
        temp=defaultdict(list)     
        def dfs (node, h):
            if not node: 
                temp[h].append("NULL")
                return
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            temp[h].append(node.val)
            return temp
        a = dfs (p,0)
        c=a.copy()
        print(c)
        temp.clear()
        b = dfs (q,0)
        print(b)
        if b==c: return True
        else: return False
        
        