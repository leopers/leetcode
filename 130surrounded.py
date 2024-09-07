#Importing list
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(board, x, y):
            if x >=len(board) or x<0 or y>=len(board[0]) or y<0:
                return
            if board[x][y] == "O":
                board[x][y] = "L"
                dfs(board, x+1, y)
                dfs(board, x, y+1)
                dfs(board, x-1, y)
                dfs(board, x, y-1)

        rows = len(board)
        cols = len(board[0])
        
        for j in range(cols):
            dfs(board, 0, j)
            dfs(board, rows-1, j)
        
        for i in range(1, rows-1):
            dfs(board, i, 0)
            dfs(board, i, cols-1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                
                if board[i][j] == "L":
                    board[i][j] = "O"
        