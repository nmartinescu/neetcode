class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        L = 0
        maximum_size = 0
        for R in range(len(s)):
            while s[R] in hash_set:
                hash_set.remove(s[L])
                L += 1
            hash_set.add(s[R])
            maximum_size = max(maximum_size, R - L + 1)
        return maximum_size