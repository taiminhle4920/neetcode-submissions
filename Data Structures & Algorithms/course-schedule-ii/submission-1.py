class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for c,p in prerequisites:
            prereq[c].append(p)
        
        visited = set()
        cycle = set()
        output = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for p in prereq[crs]:
                if not dfs(p):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []

        return output
