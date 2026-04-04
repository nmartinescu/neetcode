class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        d2 = 1
        d1 = 2
        for i in range(3, n + 1):
            aux = d1 + d2
            d2 = d1
            d1 = aux

        return d1