class Solution:
    def isValidBST(self, tree: Optional[TreeNode]) -> bool:
        def valid(node,left,right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            return valid(node.left,left,node.val) and valid(node.right,node.val,right)
        return valid(tree,float("-inf"),float("inf"))
            
