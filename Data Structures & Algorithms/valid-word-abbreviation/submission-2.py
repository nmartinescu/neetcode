class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word):
            if abbr[j].isnumeric():
                number = 0
                if abbr[j] == '0':
                    return False
                while j < len(abbr) and abbr[j].isnumeric():
                    number = number * 10 + int(abbr[j])
                    j += 1
                i += number
                if i > len(word):
                    return False
            elif j < len(abbr) and word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
        return j == len(abbr)


