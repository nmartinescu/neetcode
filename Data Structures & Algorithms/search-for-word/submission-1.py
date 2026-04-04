class Solution:

    def search(self, pos, board, word):
        n = len(board)
        m = len(board[0])
        dx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if word == "":
            return True
        save = board[pos[0]][pos[1]]
        board[pos[0]][pos[1]] = -1
        for d in dx:
            aux = (pos[0] + d[0], pos[1] + d[1])
            print("AUX", aux)
            if 0 <= aux[0] <= n - 1 and 0 <= aux[1] <= m - 1 and board[aux[0]][aux[1]] == word[0]:
                if self.search(aux, board, word[1:]):
                    return True
        board[pos[0]][pos[1]] = save
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if ch == word[0]:
                    print((i, j))
                    if self.search((i, j), board, word[1:]):
                        return True
        return False