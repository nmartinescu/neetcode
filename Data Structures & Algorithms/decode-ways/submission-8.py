class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev, curr = 1, 1
        for i in range(2, n + 1):
            digit = int(s[i - 1])
            temp = 0
            if digit != 0:
                temp = curr
            
            digit = int(s[i - 2:i])
            if 10 <= digit <= 26:
                temp += prev
            prev, curr = curr, temp
        return curr