class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers = collections.defaultdict(int)
        for num in nums:
            numbers[num] += 1
        maximum = -1
        for [key, value] in numbers.items():
            if value == 1 and key > maximum:
                maximum = key
        return maximum