class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        L = 0
        maximum = 0
        maxF = 0
        for R in range(len(s)):
            hash_map[s[R]] = hash_map.get(s[R], 0) + 1
            maxF = max(maxF, hash_map[s[R]])
            while R - L + 1 - maxF > k:
                hash_map[s[L]] -= 1
                L += 1
            maximum = max(maximum, R - L + 1)
        return maximum 