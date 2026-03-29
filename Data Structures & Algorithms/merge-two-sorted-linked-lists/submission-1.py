# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        
        head = list1
        if list2.val < head.val:
            head = list2
            list2 = list2.next
        else:
            list1 = list1.next

        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return head

