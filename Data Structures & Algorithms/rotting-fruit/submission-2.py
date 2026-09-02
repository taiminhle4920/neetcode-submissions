class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        queue = deque([])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    count += 1
                elif grid[x][y] == 2:
                    queue.append((x,y))
        if count == 0:
            return 0
        res = -1
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        count -= 1
                        queue.append((nx, ny))
                    
            res += 1
        if count > 0:
            return -1

        return res