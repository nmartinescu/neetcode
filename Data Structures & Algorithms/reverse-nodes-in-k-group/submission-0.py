# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        curr = head
        index = 0
        group_start = head
        prev_group_stop = None
        while curr:
            index += 1
            if index % k == 0:
                group_stop = curr
                curr_node = group_start
                prev = group_stop.next
                while index:
                    next_node = curr_node.next
                    curr_node.next = prev
                    prev = curr_node
                    curr_node = next_node 
                    index -= 1
                if not new_head:
                    new_head = group_stop
                if prev_group_stop:
                    prev_group_stop.next = group_stop
                prev_group_stop = group_start
                curr = group_start
                group_start = curr.next
            curr = curr.next
        return new_head
