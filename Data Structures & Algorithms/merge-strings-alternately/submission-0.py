class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, turn = 0, 0, 0
        ans = []
        while i < len(word1) and j < len(word2):
            if not turn:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
            turn = 1 - turn
        while i < len(word1):
            ans.append(word1[i])
            i += 1
        while j < len(word2):
            ans.append(word2[j])
            j += 1
        return "".join(ans)