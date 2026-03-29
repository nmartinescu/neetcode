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
            return self._hash[key]
        return -1

    def remove(self):
        to_delete = self.head.next
        if to_delete != self.tail:
            print("HE", to_delete.value, self._hash)
            del self._hash[to_delete.value]
            self.head.next = to_delete.next
            to_delete.next.prev = self.head

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

    def put(self, key: int, value: int) -> None:
        if key in self._hash:
            self._hash[key] = value
            self.upgrade(key)
            return

        if self.size == self.capacity:
            self.remove()

        self._hash[key] = value
        self.size += 1
        node = Node(key)
        self._hash_node[key] = node
        self.push_back(node)
