class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, res = 0, float("inf")
        b, w = 0, 0
        for r in range(len(blocks)):
            if blocks[r] == "B":
                b += 1
            else:
                w += 1
            
            if r - l + 1 > k:
                if blocks[l] == "B":
                    b -= 1
                else:
                    w -= 1
                l += 1
            
            if r - l + 1 == k:
                res = min(res, w)

        return res