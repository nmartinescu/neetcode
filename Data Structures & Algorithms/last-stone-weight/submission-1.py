class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            if first == second:
                continue
            else:
                heapq.heappush(heap, -second + first)
        return -heap[0] if heap else 0