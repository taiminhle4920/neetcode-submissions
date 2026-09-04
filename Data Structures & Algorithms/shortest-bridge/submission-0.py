class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        def invalid(r, c):
            return r not in range(N) or c not in range(N)

        visit = set()

        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))
            for dr, dc in direction:
                dfs(r+dr, c+dc)

        def bfs():
            res, q = 0, deque(visit)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direction:
                        nr, nc = r+dr, c+dc
                        if invalid(nr, nc) or (nr, nc) in visit:
                            continue

                        if grid[nr][nc]:
                            return res
                        q.append((nr, nc))
                        visit.add((nr, nc))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
