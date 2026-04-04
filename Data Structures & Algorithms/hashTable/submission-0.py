class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self._hash = [None] * self.capacity
    

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        node = self._hash[index]

        if not node:
            self._hash[index] = Node(key, value) 
            self.size += 1
        else:
            prev = None
            while node and node.key != key:
                prev = node
                node = node.next
            if node:
                node.value = value
            elif prev:
                prev.next = Node(key, value)
                self.size += 1
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity
        node = self._hash[index]
        while node and node.key != key:
            node = node.next
        return node.value if node else -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        node = self._hash[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self._hash[index] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        self.size = 0
        self._old_hash = self._hash
        self._hash = [None] * self.capacity
        for node in self._old_hash:
            if node:
                self.insert(node.key, node.value)
        
