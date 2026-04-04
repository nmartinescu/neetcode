class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n, m = len(words), len(words[0])
        for i in range(n):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True