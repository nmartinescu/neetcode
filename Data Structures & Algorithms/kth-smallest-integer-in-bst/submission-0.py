# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.left = k
        def inorder(root):
            if not root:
                return -1
            
            val = inorder(root.left)
            if val != -1:
                return val
            
            self.left -= 1
            if not self.left:
                return root.val
            
            return inorder(root.right)

        return inorder(root)