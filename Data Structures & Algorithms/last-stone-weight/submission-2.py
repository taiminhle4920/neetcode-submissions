class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            s1, s2 = heapq.heappop(max_heap), heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(s2-s1))
        return -(max_heap[-1])