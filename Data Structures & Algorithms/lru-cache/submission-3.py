class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.push_back(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.push_back(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def remove(self, node):
        node.next.prev, node.prev.next = node.prev, node.next

    def push_back(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next, self.tail.prev = node, node
