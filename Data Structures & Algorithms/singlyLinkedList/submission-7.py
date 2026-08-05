class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = ListNode(-1)
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        
    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values