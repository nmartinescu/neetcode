class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        r = n - 2
        while r >= 0 and nums[r] >= nums[r + 1]:
            r -= 1
        if r >= 0:
            r_next = n - 1
            while nums[r] >= nums[r_next] and r <= r_next:
                r_next -= 1
            nums[r], nums[r_next] = nums[r_next], nums[r]
        l, r = r + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums