class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(heap)
        ans = 0
        while len(heap) > 1:
            val1, val2 = heapq.heappop(heap), heapq.heappop(heap)
            ans += val1 + val2
            heapq.heappush(heap, val1 + val2)
        return ans