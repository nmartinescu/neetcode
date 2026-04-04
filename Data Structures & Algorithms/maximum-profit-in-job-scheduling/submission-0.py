import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        end_time_lambda = lambda element: element[1]
        elements = sorted(zip(startTime, endTime, profit), key=end_time_lambda)
        n = len(elements)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            start, profit = elements[i - 1][0], elements[i - 1][2]
            prev_index = bisect.bisect_right(elements, start, key=end_time_lambda, hi=i-1)
            dp[i] = max(dp[i - 1], dp[prev_index] + profit)
        return max(dp)