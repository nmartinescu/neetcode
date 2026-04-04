class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        curr_seq = 0
        for num in nums:
            if num:
                curr_seq += 1
                max_seq = max(max_seq, curr_seq)
            else:
                curr_seq = 0
        return max_seq