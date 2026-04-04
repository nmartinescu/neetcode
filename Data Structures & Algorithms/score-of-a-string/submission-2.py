class Solution:
    def scoreOfString(self, s: str) -> int:
        prev, ans = None, 0
        for c in s:
            ans, prev = ans + abs(ord(c) - ord(prev)) if prev else 0, c
        return ans