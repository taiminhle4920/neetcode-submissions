class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for p, v in prerequisites:
            adj[p].append(v)
        visited = set()
        def dfs(crs):
            if adj[crs] == []:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for i in adj[crs]:
                if not dfs(i):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


                