class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = ListNode(-1)
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while i <= index and curr:
            curr = curr.next
            i += 1
        
        if curr == None:
            return -1
        
        return curr.value

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)

        if self.head == self.tail:
            self.tail = newNode
        else:
            newNode.next = self.head.next
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while i < index and curr != None:
            curr = curr.next
            i += 1
        
        if curr != None and curr.next != None:
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        values = []

        curr = self.head
        while curr != None:
            curr = curr.next
            if curr != None:
                values.append(curr.value)
        
        return values
        
