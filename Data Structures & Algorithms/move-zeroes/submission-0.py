class Solution:
    def moveZeroes(self, nums: List[int]):
        last_non_zero_index, index = 0, 0
        while index < len(nums):
            if nums[index]:
                nums[last_non_zero_index], nums[index] = nums[index], nums[last_non_zero_index]
                last_non_zero_index += 1
            index += 1
        