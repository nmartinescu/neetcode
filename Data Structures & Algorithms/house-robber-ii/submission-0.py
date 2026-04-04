class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        dp = [(0, 0)] * n
        dp[0] = (nums[0], 0)
        dp[1] = (max(nums[0], nums[1]), nums[1])
        for i in range(2, n):
            dp[i] = (
                max(dp[i - 1][0], nums[i] + dp[i - 2][0]), 
                max(dp[i - 1][1], nums[i] + dp[i - 2][1])
            )
        return max(dp[n - 1][1], dp[n - 2][0])