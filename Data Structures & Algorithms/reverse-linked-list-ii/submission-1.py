# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, node, length):
        prev, start = None, node
        while node and length:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node 
            length -= 1
        start.next = node
        return prev


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        length = right - left + 1
        if left == 1:
            return self.reverse(head, length)
        
        curr = head
        i = 1
        while curr and i + 1 != left:
            i += 1
            curr = curr.next
        
        curr.next = self.reverse(curr.next, length)
        return head