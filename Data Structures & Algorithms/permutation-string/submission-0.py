from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        s1_hash = Counter(s1)
        s2_hash = Counter()
        L = 0
        for R in range(len(s2)):
            s2_hash[s2[R]] += 1
            if R >= n1:                
                if s2_hash[s2[L]] == 1:
                    del s2_hash[s2[L]]
                else:
                    s2_hash[s2[L]] -= 1
                L += 1
            if s1_hash == s2_hash:
                return True
        return False