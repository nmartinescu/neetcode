class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] % 2 == 1:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                i -= 1
            i += 1
        return nums
