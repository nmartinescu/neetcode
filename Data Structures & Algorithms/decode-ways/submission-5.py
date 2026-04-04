class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dp(i):
            if s[:i + 1] in cache:
                return cache[s[:i + 1]]
            
            if i == 0:
                return int("1" <= s[i] <= "9")
            elif i == 1:
                curr = 0
                if "1" <= s[i] <= "9":
                    curr += dp(i - 1)
                if "1" <= f"{s[i-1]}{s[i]}" <= "26":
                    curr += 1
                cache[s[:2]] = curr
                return cache[s[:2]]

            curr = 0
            if "1" <= s[i] <= "9":
                curr += dp(i - 1)
            if "1" <= f"{s[i-1]}{s[i]}" <= "26":
                curr += dp(i - 2)
            cache[s[:i + 1]] = curr
            return cache[s[:i + 1]]
                
        return dp(len(s) - 1)