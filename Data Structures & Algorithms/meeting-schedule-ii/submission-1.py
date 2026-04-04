"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        intervals.sort(key=lambda i: i.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            earliest = heap[0]
            if intervals[i].start >= earliest:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        return len(heap)