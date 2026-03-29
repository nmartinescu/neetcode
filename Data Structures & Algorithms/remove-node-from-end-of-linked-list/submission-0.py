# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            return None
        slow = fast = head
        while fast and n + 1:
            fast = fast.next
            n -= 1
        if n + 1:
            head = head.next
            return head
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        