class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        maxV = 0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]


        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1
            while q:
                row, col = q.popleft()
                
                for dr, dc in direction:
                    r, c = row +dr, col+dc
                    if (r < 0 or c < 0 or r >= ROWS or
                    c >= COLS or grid[r][c] == 0):
                        continue
                    res += 1
                    q.append((r,c))
                    grid[r][c] = 0
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxV = max(maxV, bfs(r,c))
                    
        return maxV