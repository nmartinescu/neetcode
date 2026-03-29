class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        mergedInterval = None
        if i < len(intervals) and intervals[i][0] <= newInterval[0] <= intervals[i][1]:
            mergedInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
            while i < len(intervals) and mergedInterval[0] <= intervals[i][0] <= mergedInterval[1]:
                mergedInterval = [min(mergedInterval[0], intervals[i][0]), max(mergedInterval[1], intervals[i][1])]
                i += 1 
        if mergedInterval:
            ans.append(mergedInterval)
        else:
            ans.append(newInterval)
        while i < len(intervals):
            ans.append(intervals[i])    
            i += 1
        return ans
