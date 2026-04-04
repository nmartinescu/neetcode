"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def dfs(self, node: Optional['Node'], visit) -> Optional['Node']:
        if node in visit:
            return visit[node]
        new_node = Node(node.val)
        visit[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.dfs(neighbor, visit))
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {}) if node else None