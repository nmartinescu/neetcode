class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = 0
        n = len(strs)

        while True:
            ch = None
            found = True
            if lcp < len(strs[0]):
                ch = strs[0][lcp]
            else:
                break
            for i in range(1, n):
                if lcp == len(strs[i]) or ch != strs[i][lcp]:
                    found = False
                    break
            if not found:
                break
            lcp += 1
        return "" if lcp == -1 else strs[0][:lcp]