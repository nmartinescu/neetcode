class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        dp[0] = int("1" <= s[0] <= "9")
        if len(s) >= 2:
            dp[1] = dp[0] if "1" <= s[1] <= "9" else 0
            dp[1] += 1 if "1" <= f"{s[0]}{s[1]}" <= "26" else 0

            for i in range(2, len(s)):
                if "1" <= s[i] <= "9":
                    dp[i] += dp[i - 1]
                if "1" <= f"{s[i-1]}{s[i]}" <= "26":
                    dp[i] += dp[i - 2]
        
        return dp[len(s) - 1]