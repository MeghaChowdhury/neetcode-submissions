class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #let's start with rows
        for r in range(9):
            seen = set()
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)  

        #checking in columns
        for c in range(9):
            seen = set()

            for r in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                if value in seen:
                    return False

                seen.add(value)
        #checking the 3x3 boxes
        for box_row in range(0,9,3):
            for box_column in range(0,9,3):
                seen = set()

                for r in range(box_row , box_row + 3):
                    for c in range(box_column, box_column + 3):
                        value = board[r][c]

                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
        return True
