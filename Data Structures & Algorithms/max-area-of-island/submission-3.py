class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        
        def bfs(x, y):
            direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            cur = 0
            queue = deque([(x, y)])
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    visited.add((x, y))
                    cur += 1
                    for dx, dy in direction:
                        nx, ny = x+dx, y+dy
                        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                            continue
                        if grid[nx][ny] == 0 or (nx, ny) in visited:
                            continue
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return cur
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0 or (x,y) in visited:
                    continue
                temp = bfs(x,y)
                res = max(res, temp)
        return res
        
