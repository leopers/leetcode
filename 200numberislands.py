import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0

        def dfs(grid, x, y):
            dirs = {(1,0), (0, 1), (-1, 0), (0, -1)}

            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] == "1":
                grid[x][y] = "X"
                for i, j in dirs:
                    dfs(grid, x+i, y+j)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    num += 1
                    dfs(grid, i, j)

        return num