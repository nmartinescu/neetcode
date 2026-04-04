class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        appears = set(nums)
        visited = set()
        max_size = 0
        for num in nums:
            if num - 1 in appears or num in visited:
                continue
            size = 0
            n = num
            while n in appears:
                size += 1
                n += 1
            max_size = max(max_size, size)
            visited.add(num)
        return max_size