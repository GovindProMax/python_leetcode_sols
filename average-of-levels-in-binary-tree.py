# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sumdict=defaultdict(float)
        numdict=defaultdict(int)
        
        def dfs (node, h):
            if not node: return
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            sumdict[h]+=node.val
            numdict[h]+=1
            print("Added ", node.val)
            print("at height ", h)
        
        dfs (root,0)
        print(sumdict)
        print(numdict)
        
        return [sumdict[i]/numdict[i] for i in range(len(sumdict))]