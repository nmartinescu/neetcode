class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        n = len(nums)
        for i in range(1 << n):
            bitset = i
            j = 0
            current = []
            while bitset:
                if bitset & 1:
                    current.append(nums[j])
                bitset >>= 1
                j += 1
            sol.append(current)
        return sol