class Solution:

    def check(self, piles: List[int], val: int, h: int):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(float(pile) / val)
        return total_time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l < r:
            m = l + (r - l) // 2
            if self.check(piles, m, h):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res