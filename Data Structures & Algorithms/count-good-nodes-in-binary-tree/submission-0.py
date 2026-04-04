# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, greatest):
            if not node:
                return 0
            
            isGood = 0
            if node.val >= greatest:
                isGood = 1
            greatest = max(greatest, node.val)
            left = dfs(node.left, greatest)
            right = dfs(node.right, greatest)
            return isGood + left + right
        return dfs(root, float("-inf"))