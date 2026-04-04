"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def dfs(self, node: Optional['Node'], visit) -> Optional['Node']:
        new_node = Node(node.val)
        visit[node] = new_node

        new_neighbors = []
        for neighbor in node.neighbors:
            if neighbor not in visit:
                self.dfs(neighbor, visit)
            new_neighbors.append(visit[neighbor])
        new_node.neighbors = new_neighbors
        return new_node


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {}) if node else None