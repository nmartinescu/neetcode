class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length % 2 == 0:
            if self.minHeap and self.minHeap[0] < num:
                top = heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
                num = top
            heapq.heappush(self.maxHeap, -num)
        else:
            if self.maxHeap and num < -self.maxHeap[0]:
                top = heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, -num)
                num = -top
            heapq.heappush(self.minHeap, num)
        self.length += 1


    def findMedian(self) -> float:
        if self.length % 2:
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        