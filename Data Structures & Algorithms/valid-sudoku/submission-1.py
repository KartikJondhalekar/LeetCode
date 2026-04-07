class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        n = len(board)
        
        for row in range(n):
            for col in range(n):
                num = board[row][col]
                if num.isdecimal():
                    if (row, num) in seen or (num, col) in seen or (row // 3, col //3, num) in seen:
                        return False
                    else:
                        seen.add((row, num))
                        seen.add((num, col))
                        seen.add((row // 3, col //3, num))
                        
        return True