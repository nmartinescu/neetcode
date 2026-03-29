class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        L, R = 0, 0
        curSum = 0
        maxSum = nums[0]
        n = len(nums)

        while R < n or (curSum >= 0 and R % n < L):
            if curSum < 0:
                curSum = 0
                L = R
            index = R % n
            curSum += nums[index]
            maxSum = max(maxSum, curSum)
            R += 1
        return maxSum
            
            