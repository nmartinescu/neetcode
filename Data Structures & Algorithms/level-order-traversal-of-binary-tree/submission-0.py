# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        queue = deque()
        if root:
            queue.append(root)

        while len(queue):
            current_level = []
            current_level_length = len(queue)
            for _ in range(current_level_length):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sol.append(current_level)
        return sol