class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        for ch in s:
            s_hash[ch] = s_hash.get(ch, 0) + 1
        for ch in t:
            if ch not in s_hash:
                return False
            else:
                if s_hash[ch] == 1:
                    del s_hash[ch]
                else:
                    s_hash[ch] -= 1
        return len(s_hash) == 0