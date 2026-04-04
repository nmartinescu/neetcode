class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        
        idx = 0
        while zeros:
            nums[idx] = 0
            idx += 1
            zeros -= 1
        while ones:
            nums[idx] = 1
            idx += 1
            ones -= 1
        while twos:
            nums[idx] = 2
            idx += 1
            twos -= 1
