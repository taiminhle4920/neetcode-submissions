class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        def dfs(x, y):
            if x <0 or x >= len(grid):
                return
            if y < 0 or y >= len(grid[0]):
                return
            if grid[x][y] == "0" or (x, y) in visited:
                return 
            visited.add((x, y))
            dfs(x+1, y)
            dfs(x-1,y)
            dfs(x, y-1)
            dfs(x, y+1)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "0" or (x,y) in visited:
                    continue
                res += 1
                dfs(x,y)
        return res
