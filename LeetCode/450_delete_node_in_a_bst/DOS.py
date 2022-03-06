from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            root.val = self.get_next_val(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root
            
            
    def get_next_val(self, root):
        if not root:
            return None
        if not root.left:
            return root.val
        return self.get_next_val(root.left)