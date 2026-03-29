# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        idx1, idx2, head = list1, list2, None
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val < list2.val:
            head = list1
        else:
            head = list2

        while idx1 != None and idx2 != None:
            if idx1.val < idx2.val:
                while idx1 != None and idx1.next != None and idx1.next.val < idx2.val:
                    idx1 = idx1.next

                next_aux = idx1.next
                idx1.next = idx2
                idx1 = next_aux
            else:
                while idx2 != None and idx2.next != None and idx2.next.val < idx1.val:
                    idx2 = idx2.next

                next_aux = idx2.next
                idx2.next = idx1
                idx2 = next_aux
        
        return head