class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.partial = [[0 for _ in range(m)] for _ in range(n)]
        self.partial[0][0] = matrix[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    self.partial[i][j] = self.partial[i][j - 1] + matrix[i][j]
                elif j == 0:
                    self.partial[i][j] = self.partial[i - 1][j] + matrix[i][j]
                else:
                    self.partial[i][j] = self.partial[i - 1][j] + self.partial[i][j - 1] - self.partial[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.partial[row2][col2]
        elif row1 == 0:
            return self.partial[row2][col2] - self.partial[row2][col1 - 1]
        elif col1 == 0:
            return self.partial[row2][col2] - self.partial[row1 - 1][col2]
        else:
            return self.partial[row2][col2] - self.partial[row2][col1 - 1] - self.partial[row1 - 1][col2] + self.partial[row1 - 1][col1 - 1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)