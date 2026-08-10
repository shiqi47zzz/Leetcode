'''
542. 01 Matrix
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                if mat[r][c] == 1:
                    mat[r][c] = -1
        
        direction = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in direction:
                nr = dr + r
                nc = dc + c

                if (
                    0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1
                ):
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr,nc))
        return mat
                    
                


