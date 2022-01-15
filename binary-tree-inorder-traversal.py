# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        if root:
            elements = elements + self.inorderTraversal(root.left)
            elements.append(root.val)
            elements = elements + self.inorderTraversal(root.right)
        return elements
        