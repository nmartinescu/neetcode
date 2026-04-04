class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pairs = []
        n = len(nums)
        for val in nums:
            l, r, sol = 0, len(pairs) - 1, 0
            while l <= r:
                m = (l + r) // 2
                if pairs[m] < val:
                    l = m + 1
                    sol = m + 1
                else:
                    r = m - 1
            if sol == len(pairs):
                pairs.append(val)
            elif val < pairs[sol]:
                pairs[sol] = val
        return len(pairs)