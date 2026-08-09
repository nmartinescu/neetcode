class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.visiting = self.head

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.next = self.tail
        new_node.prev = self.visiting
        self.tail.prev = new_node
        self.visiting.next = new_node
        self.visiting = self.visiting.next

    def back(self, steps: int) -> str:
        while steps and self.visiting != self.head:
            self.visiting = self.visiting.prev
            steps -= 1
        return self.visiting.val

    def forward(self, steps: int) -> str:
        while steps and self.visiting.next != self.tail:
            self.visiting = self.visiting.next
            steps -= 1
        return self.visiting.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)