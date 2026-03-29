class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self._hash = {}
        self._hash_node = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self._hash:
            self.upgrade(key)
            return self._hash[key]
        return -1

    def pop_front(self):
        node = self.head.next
        if node == self.tail:
            return
        del self._hash[node.value]
        self.head.next = node.next
        node.next.prev = self.head
        self.size -= 1

    def upgrade(self, key):
        node = self._hash_node[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        self.push_back(node)
    
    def push_back(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def put(self, key: int, value: int) -> None:
        if key in self._hash:
            self._hash[key] = value
            self.upgrade(key)
            return

        if self.size == self.capacity:
            self.pop_front()

        self._hash[key] = value
        node = Node(key)
        self._hash_node[key] = node
        self.push_back(node)
