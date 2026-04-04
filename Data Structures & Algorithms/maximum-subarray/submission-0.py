class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            if curSum > maxSum:
                maxSum = curSum
        return maxSum