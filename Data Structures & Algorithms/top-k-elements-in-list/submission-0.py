class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        counts = defaultdict(list)
        for num in nums:
            freq[num] += 1
        for key in freq:
            value = freq[key]
            counts[value].append(key)
        sol = []
        n = 10000
        while len(sol) < k:
            if n in counts:
                sol += counts[n]
            n -= 1
        return sol