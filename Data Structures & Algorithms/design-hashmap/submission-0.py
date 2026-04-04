class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self._capacity = 769
        self._buckets = [Node((-1, -1))] * self._capacity

    def put(self, key: int, value: int) -> None:
        bucket = key % self._capacity
        if self.get(key) != -1:
            curr = self._buckets[bucket].next
            while curr:
                if curr.value[0] == key:
                    curr.value = (key, value)
                curr = curr.next
        else:
            head = self._buckets[bucket]
            head.next = Node((key, value), head.next)
            

    def get(self, key: int) -> int:
        bucket = key % self._capacity
        curr = self._buckets[bucket].next
        while curr:
            if curr.value[0] == key:
                return curr.value[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        bucket = key % self._capacity
        prev = self._buckets[bucket]
        curr = self._buckets[bucket].next
        while curr:
            if curr.value[0] == key:
                prev.next = curr.next
            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)