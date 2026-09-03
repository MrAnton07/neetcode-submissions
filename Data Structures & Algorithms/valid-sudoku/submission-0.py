from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def counter_3x3(i, j, board) -> bool:
            arr = []
            for row in range(i, i+3):
                for col in range(j, j+3):
                    val = board[row][col]
                    if val != ".":
                        arr.append(board[row][col])
            # val = any(value > 1 for _, value in Counter(arr).items())    
            # print(val, i, j)
            return any(value > 1 for _, value in Counter(arr).items())

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if (counter_3x3(i, j, board)):
                    return False
        
        for row in board:
            if any( ((value > 1) and (key!="."))  for key, value in Counter(row).items()):
                return False

        for col in zip(*board):
            if any( ((value > 1) and (key != ".")) for key, value in Counter(col).items() ):
                return False
        return True