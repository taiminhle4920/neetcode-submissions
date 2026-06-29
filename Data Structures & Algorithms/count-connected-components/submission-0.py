class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        adj = [[] for _ in range(n)]
        res = 0
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        return res