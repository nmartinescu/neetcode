class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j, ans = 0, 0, 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                j += 1
                ans += 1
            i += 1
                
        return ans