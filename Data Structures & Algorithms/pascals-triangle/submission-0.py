class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            triangle = [[1], [1, 1]]
            for i in range(2, numRows):
                triangle.append([1])
                for j in range(1, i):
                    triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
                triangle[i].append(1)
        return triangle