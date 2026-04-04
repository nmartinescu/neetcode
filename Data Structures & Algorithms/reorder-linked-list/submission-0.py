# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr, prev = slow, None
        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        l, r = head, prev
        turn = 0
        while l != slow and r:
            aux = None
            if not turn:
                aux = l.next
                l.next = r
                l = aux
            else:
                aux = r.next
                r.next = l
                r = aux
            turn = 1 - turn
