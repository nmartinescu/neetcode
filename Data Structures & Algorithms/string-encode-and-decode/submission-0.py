class Solution:

    def encode(self, strs: List[str]) -> str:
        str_list = []
        for strings in strs:
            str_list.append(str(len(strings)))
            str_list.append("#")
            str_list.append(strings)
        return "".join(str_list)
    
    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            number = 0
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                number = number * 10 + ord(s[i]) - ord('0')
                i += 1
            i += 1
            new_str = []
            while i < len(s) and number:
                new_str.append(s[i])
                i += 1
                number -= 1
            ans.append("".join(new_str))
        return ans
