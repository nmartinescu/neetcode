class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDictSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if dp[j] and sub in wordDict:
                    dp[i] = True
                    break
        return dp[n]