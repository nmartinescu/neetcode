class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        for index, num in enumerate(nums):
            r -= num
            if l == r:
                return index
            l += num
        return -1