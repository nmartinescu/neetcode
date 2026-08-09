class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head 

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while i < index and curr != self.tail:
            curr = curr.next
            i += 1
        if curr != self.tail:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        i = 0
        curr = self.head
        while i < index and curr != self.tail:
            curr = curr.next
            i += 1
        
        if curr != self.tail:
            new_node.next = curr.next
            new_node.prev = curr
            curr.next.prev = new_node
            curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head
        while i < index and curr != self.tail:
            i += 1
            curr = curr.next

        if curr != self.tail and curr.next != self.tail:
            curr.next.next.prev = curr
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)