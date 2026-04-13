class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        L, R = 0, len(nums) - 1
        sol = -1
        while L < R:
            sum = nums[L] + nums[R]
            if sum >= k:
                R -= 1
            else:
                sol = max(sol, sum)
                L += 1
        return sol
                