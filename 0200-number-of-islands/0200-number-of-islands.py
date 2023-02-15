class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # counter
        counter = 0
        visited = set()
        # traverse grid
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1' and (row,col) not in visited:
                    counter += 1 
                    self.dfs(grid,row,col, visited)
                        
        
        return counter
    

    def dfs(self, grid, row, col, visited):
        print(row, col)
        visited.add((row,col))
        directions = [[-1,0],[1, 0],[0,-1],[0,1]]
        for dir in directions:
            newRow = row + dir[0]
            newCol = col + dir[1]
            if (newRow >= 0 and newRow < len(grid)) and (newCol >= 0 and newCol < len(grid[0])) and (grid[newRow][newCol] == '1' and (newRow, newCol) not in visited):
                visited.add((newRow, newCol))
                self.dfs(grid, newRow, newCol, visited)
            