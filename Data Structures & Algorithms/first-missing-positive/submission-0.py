class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums):
            num = nums[index]
            if num > 0 and num <= len(nums) and num != index + 1 and num != nums[num - 1]:
                nums[index], nums[num - 1] = nums[num - 1], nums[index]
                continue
            index += 1
        for index, num in enumerate(nums):
            if num != index + 1:
                return index + 1
        return len(nums) + 1