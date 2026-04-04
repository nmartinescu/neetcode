class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet, subsets = [], []
        self.helper(0, nums, curSet, subsets)
        return subsets
    
    def helper(self, i, nums, curSet, subsets):
        if i == len(nums):
            subsets.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, subsets)
        curSet.pop()

        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
        self.helper(i + 1, nums, curSet, subsets)