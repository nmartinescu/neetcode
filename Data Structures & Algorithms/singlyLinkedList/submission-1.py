class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = None
    

    def get(self, index: int) -> int:
        i = 0
        curr = self.head

        while curr != None and i < index:
            curr = curr.next
        
        if curr != None:
            return curr.value
        return -1


    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        if index == 0:
            if self.head == None:
                return False
            else:
                if self.head == self.tail:
                    self.head = self.tail = self.head.next
                else:
                    self.head = self.head.next
                return True

        while curr != None and i < index - 1:
            curr = curr.next
            i += 1
        
        if curr == None:
            return False
        
        if self.tail == curr.next:
            self.tail = curr
        curr.next = curr.next.next
        return True
        

    def getValues(self) -> List[int]:
        values = []

        curr = self.head
        while curr != None:
            values.append(curr.value)
            curr = curr.next
        
        return values
