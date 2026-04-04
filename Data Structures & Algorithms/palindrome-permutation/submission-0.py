class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        appears, odd = collections.defaultdict(int), False
        for ch in s:
            appears[ch] += 1
        for values in appears.values():
            if values % 2 == 1 and odd:
                return False
            elif values % 2 == 1:
                odd = True
        return True