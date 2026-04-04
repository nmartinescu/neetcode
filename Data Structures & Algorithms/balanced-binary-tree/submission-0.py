# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0, True
            
            left, left_ok = dfs(node.left)
            right, right_ok = dfs(node.right)

            if not left_ok or not right_ok:
                return 0, False
            
            if abs(left - right) > 1:
                return 0, False
            return 1 + max(left, right), True
        return dfs(root)[1]