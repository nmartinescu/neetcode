"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {}
        curr, prev, new_head = head, None, None
        while curr:
            new_node = Node(curr.val)
            if prev:
                hash[prev].next = new_node
            else:
                new_head = new_node
            hash[curr] = new_node
            prev = curr
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                hash[curr].random = hash[curr.random]
            curr = curr.next
        return new_head