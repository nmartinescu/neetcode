# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, i = None, head
        while i:
            # reverse current node
            temp = i.next
            i.next = prev

            j, j_prev, prev = i.next, i, i.next
            while j and j.val > i.val:
                j_prev = j
                j = j.next

            # if a larger element exists
            if j_prev != i:
                i.next = j_prev.next
                j_prev.next = i
            else:
                prev = i
            i = temp
        
        # reverse list
        head, prev = prev, None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev