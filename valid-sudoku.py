class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res=[]
        for row in range(0,len(board)):
            if self.isValidArray(board[row]) == False:
                return False
            if self.isValidArray([rowc[row] for rowc in board]) == False:
                return False
        for row in range(0,9,3):
            for column in range(0,9,3):
                res=[board[row][column],board[row][column+1],board[row][column+2],board[row+1][column],board[row+1][column+1],board[row+1][column+2],board[row+2][column],board[row+2][column+1],board[row+2][column+2]]
                print(res)
                if self.isValidArray(res) == False:
                    return False
        return True