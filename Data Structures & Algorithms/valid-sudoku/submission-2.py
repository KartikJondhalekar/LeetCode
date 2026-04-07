class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        n = len(board)
        
        for row in range(n):
            for col in range(n):
                num = board[row][col]
                if num.isdecimal():
                    if ('r', row, num) in seen or ('c', col, num) in seen or ('b', row // 3, col //3, num) in seen:
                        return False
                    else:
                        seen.add(('r', row, num))
                        seen.add(('c', col, num))
                        seen.add(('b', row // 3, col //3, num))
                        
        return True