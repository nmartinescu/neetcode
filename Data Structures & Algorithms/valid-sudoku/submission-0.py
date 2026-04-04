class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        regions = {}

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == ".":
                    continue

                region = i // 3 * 3 + j // 3
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if region not in regions:
                    regions[region] = set()
                
                if element in rows[i] or element in cols[j] or element in regions[region]:
                    return False
                rows[i].add(element)
                cols[j].add(element)
                regions[region].add(element)
        return True
                