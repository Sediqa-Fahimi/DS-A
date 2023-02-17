class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        # traverse grid
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1': 
                    counter += 1 
                    self.dfs(grid, row, col) 
                        
        
        return counter
    

    def dfs(self, grid, row, col): 
       
        grid[row][col] = '0'
        directions = [[-1,0],[1, 0],[0,-1],[0,1]]
        for dir in directions:
            newRow = row + dir[0]
            newCol = col + dir[1]
            if self.inBound(grid, newRow, newCol) and grid[newRow][newCol] == '1':
                grid[newRow][newCol] = '0'
                self.dfs(grid, newRow, newCol) 
        
        
    def inBound(self, grid, i, j):
        return (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0]))
        
            