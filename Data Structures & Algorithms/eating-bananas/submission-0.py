class Solution:

    def check(self, piles: List[int], val: int, h: int):
        i = 0
        n = len(piles)
        cnt = 0

        while i < n:
            cnt += piles[i] // val + 1
            if piles[i] % val == 0:
                cnt -= 1
            i += 1
        
        return cnt <= h
            

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) + 1
        while l < r:
            m = l + (r - l) // 2
            if self.check(piles, m, h):
                r = m
            else:
                l = m + 1
        
        return l