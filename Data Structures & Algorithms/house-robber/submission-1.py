class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev, cur = 0, nums[0]
        for i in range(1, len(nums)):
            skip = cur
            take = prev + nums[i]
            prev, cur = cur, max(skip, take)
        return cur
        