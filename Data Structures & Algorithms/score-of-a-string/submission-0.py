class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = None
        ans = 0
        for c in s:
            if prev:
                ans += abs(ord(c) - ord(prev))
            prev = c
        return ans