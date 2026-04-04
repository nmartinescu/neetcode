class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def percolate_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def percolate_down(self, index: int) -> None:
        while 2 * index <= self.size:
            left = 2 * index
            right = 2 * index + 1
            if right <= self.size and \
                self.heap[index] > self.heap[right] and \
                self.heap[right] < self.heap[left]:
                self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                index = right
            elif self.heap[left] < self.heap[index]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                index = left
            else:
                break

    def push(self, val: int) -> None:
        self.size += 1
        self.heap.append(val)
        self.percolate_up(self.size)

    def pop(self) -> int:
        if self.size == 0:
            return -1
    
        removed_element = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.percolate_down(1)
        return removed_element

    def top(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap[0] = 0
        self.heap[1:] = nums
        self.size = len(nums) 

        curr = self.size // 2
        while curr:
            self.percolate_down(curr)
            curr -= 1
        
        