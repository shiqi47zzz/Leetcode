'''
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        queue = deque()
        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh > 0: #fresh need to be counted
            
            for _ in range(len(queue)):
                r,c = queue.popleft()

                direction = [
                    (1,0),(-1,0),(0,1),(0,-1)
                ]

                for dr, dc in direction:
                    nr = dr + r
                    nc = dc + c

                    if (
                        0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1 #fresh number need to be reduced
                        queue.append((nr, nc))
            
            minutes += 1
        
        return minutes if fresh == 0 else -1