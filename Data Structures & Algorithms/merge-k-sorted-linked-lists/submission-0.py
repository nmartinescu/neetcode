# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.divide(lists, 0, len(lists))

    def divide(self, lists, l, r):
        if l > r:
            return []
        elif l == r:
            return lists[l]
        
        m = (l + r) // 2
        left = self.divide(lists, l, m)
        right = self.divide(lists, m + 1, r)
        return self.conquer(left, right)
    
    def conquer(self, left, right):
        head = curr = ListNode(-1)
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return head.next