class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        m, n = len(grid), len(grid[0])
        grid[0][0] = -1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                if row < m-1 and grid[row+1][col] != 1:
                    grid[row+1][col] += grid[row][col]
                if col < n-1 and grid[row][col+1] != 1:
                    grid[row][col+1] += grid[row][col]
        
        return -grid[-1][-1]