class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)

        for num in nums:
            count[num] += 1
        for key, value in count.items():
            freq[value].append(key)
        sol = []
        n = len(nums)
        while len(sol) < k:
            if n in freq:
                sol += freq[n]
            n -= 1
        return sol