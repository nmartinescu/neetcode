from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return ""
        t_counter = Counter(t)
        s_counter = Counter()
        L, completed = 0, 0
        minimum_pos, minimum_length = -1, -1
        for R in range(n1):
            right_ch = s[R]
            s_counter[right_ch] += 1
            if right_ch in t_counter and s_counter[right_ch] == t_counter[right_ch]:
                completed += 1    
            while completed == len(t_counter) and L <= R:
                left_ch = s[L]
                if R - L + 1 < minimum_length or minimum_length == -1:
                    minimum_pos, minimum_length = L, R - L + 1
                if left_ch in t_counter and s_counter[left_ch] == t_counter[left_ch]:
                    completed -= 1
                s_counter[left_ch] -= 1
                L += 1
        if minimum_pos != -1:
            return s[minimum_pos:minimum_pos + minimum_length]
        else:
            return ""