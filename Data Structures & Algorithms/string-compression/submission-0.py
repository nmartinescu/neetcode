class Solution:
    def modify(self, chars: List[str], c: str, cnt: int, idx: int):
        chars[idx] = c
        idx += 1
        number = str(cnt)
        if cnt == 1:
            return idx
            
        for j in range(len(number)):
            chars[idx] = number[j]
            idx += 1
        return idx

    def compress(self, chars: List[str]) -> int:
        c, cnt = chars[0], 1
        idx = 0

        for i in range(1, len(chars)):
            if chars[i] == c:
                cnt += 1
            else:
                idx = self.modify(chars, c, cnt, idx)
                c, cnt = chars[i], 1
        idx = self.modify(chars, c, cnt, idx)
        return idx
        
