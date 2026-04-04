class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
class MyHashSet:

    def __init__(self):
        self._capacity = 100000
        self._buckets = [Node(-1)] * self._capacity

    def add(self, key: int) -> None:
        bucket = key % self._capacity
        if not self.contains(key):
            head = self._buckets[bucket]
            head.next = Node(key, head.next)

    def remove(self, key: int) -> None:
        bucket = key % self._capacity
        prev = self._buckets[bucket]
        curr = self._buckets[bucket].next
        while curr:
            if curr.value == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        bucket = key % self._capacity
        curr = self._buckets[bucket].next
        while curr:
            if curr.value == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)