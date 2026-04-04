class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        sum = 0
        min_length = float("inf")
        for i in range(n):
            sum += nums[i]
            while sum >= target and j <= i:
                min_length = min(min_length, i - j + 1)
                sum -= nums[j]
                j += 1
        return 0 if min_length == float("inf") else min_length