class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val==key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            p=root.right
            while p.left: p=p.left
            root.val=p.val
            root.right=self.deleteNode(root.right,root.val)
        
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)
        
        return root