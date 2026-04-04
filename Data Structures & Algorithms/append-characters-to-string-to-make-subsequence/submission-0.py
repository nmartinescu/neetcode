class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l_s, l_t = 0, 0
        while l_s < len(s) and l_t < len(t):
            if s[l_s] == t[l_t]:
                l_t += 1
            l_s += 1
        return len(t) - l_t