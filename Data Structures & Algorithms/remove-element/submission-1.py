class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        length = len(nums)
        for r in range(length):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1 
        return l