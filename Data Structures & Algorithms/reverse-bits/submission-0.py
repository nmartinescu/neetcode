class Solution:
    def reverseBits(self, n: int) -> int:
        solution = 0
        l = 31
        while n > 0:
            if n & 1:
                solution |= 1 << l
            n >>= 1
            l -= 1
        return solution