#leetcode practice question 200
#given a 2D array find how many islands are on the grid consisting of 1s, if ones are next to 
#each other they are consider a larger island

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #helper function to traverse grid when 1 is found
        def bfs(grid, col, row, i, j, vs):
            if i < 0 or i == row or j < 0 or j == col:
                return

            if grid[i][j] == "1" and (i,j) not in vs:
                vs.add((i,j))
                bfs(grid, col, row, i - 1, j, vs) #up
                bfs(grid, col, row, i + 1, j, vs) #down
                bfs(grid, col, row, i, j + 1, vs) #right
                bfs(grid, col, row, i, j - 1, vs) #left
            return
        
        
        col, row = len(grid[0]), len(grid)
        res = 0
        vs = set() 
        
        if not grid:
            return 0 

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in vs:
                    res += 1
                    bfs(grid, col, row, i, j, vs) 

        return res