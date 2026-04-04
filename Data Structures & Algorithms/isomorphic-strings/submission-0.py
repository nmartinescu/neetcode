class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for i, c in enumerate(s):
            if c in s_hash and s_hash[c] != t[i]:
                return False
            elif c not in s_hash:
                if t[i] in t_hash:
                    return False
                s_hash[c] = t[i]
                t_hash[t[i]] = c
        return True

