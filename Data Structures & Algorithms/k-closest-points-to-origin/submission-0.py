import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[-(x * x + y * y), (x, y)] for x, y in points]
        heap = []
        for point in points:
            if len(heap) < k:
                heapq.heappush(heap, point)
            elif heap[0][0] < point[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, point)
        return [point[1] for point in heap]

