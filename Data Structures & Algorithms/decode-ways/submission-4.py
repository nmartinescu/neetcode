class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dp(i):
            if s[:i + 1] in cache:
                return cache[s[:i + 1]]
            if i == 0:
                return int('1' <= s[i] <= '9')
            if i == 1:
                if s[i] == "0" and s[0] == "0":
                    return 0
                elif s[i] == "0":
                    return 1
                else:
                    return int('1' <= s[0] <= '9') + int("1" <= f"{s[i-1]}{s[i]}" <= "26")
            else:
                one_digit = dp(i - 1) if '1' <= s[i] <= '9' else 0
                two_digit = dp(i - 2) if "1" <= f"{s[i-1]}{s[i]}" <= "26" else 0
                cache[s[:i + 1]] = one_digit + two_digit if one_digit and two_digit else 0
                return cache[s[:i + 1]]
        return dp(len(s) - 1)     

        # one_digit = 1 + dp[n - 1], if s[i] in [1, 9]
        # two_digits = 1 + dp[n - 2], if s[i]s[i+1] in [1, 26]
        # dp[n] = one_digit + two_digit