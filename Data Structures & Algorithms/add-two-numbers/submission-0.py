# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second, head, prev = l1, l2, None, None
        r = 0
        while first or second or r:
            sum = 0
            if first:
                sum += first.val
            if second:
                sum += second.val
            if r:
                sum += r

            if sum > 9:
                sum -= 10
                r = 1
            else:
                r = 0
            new_node = ListNode(sum)
            if prev:
                prev.next = new_node
            else:
                head = new_node
            prev = new_node
            if first:
                first = first.next
            if second:
                second = second.next
        return head
