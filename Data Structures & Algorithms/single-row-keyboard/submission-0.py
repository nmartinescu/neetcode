class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index, sol, mapping = 0, 0, {}
        for i in range(26):
            mapping[keyboard[i]] = i
        for char in word:
            sol += math.abs(mapping[char] - index)
            index = mapping[char]
        return sol