# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float("-inf")
        def dfs(node):
            nonlocal maximum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maximum = max(maximum, node.val, left + node.val, right + node.val, left + right + node.val)
            return max(left + node.val, right + node.val)
        dfs(root)
        return maximum