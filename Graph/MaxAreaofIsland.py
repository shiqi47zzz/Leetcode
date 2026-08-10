'''
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area =  0

        def dfs(r,c):
            if (
                r < 0  or r >= rows or c < 0 or c >= cols or grid[r][c] == 0
            ):
                return 0
            
            grid[r][c] = 0
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs (r, c+1) + dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area =  max(max_area, area)

        return max_area