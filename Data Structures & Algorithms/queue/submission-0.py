class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        val = self.tail.prev.val
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
        return val
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        val = self.head.next.val
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return val
        
