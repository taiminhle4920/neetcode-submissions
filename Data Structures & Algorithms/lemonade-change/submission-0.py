class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dct = {5:0, 10:0, 20:0}
        for b in bills:
            if b == 5:
                dct[5] += 1
                continue
            elif b == 20:
                dct[20] += 1
                if dct[10] > 0 and dct[5] > 0:
                    dct[10] -= 1
                    dct[5] -= 1
                    continue
                elif dct[5] > 2:
                    dct[5] -= 3
                    continue
                else:
                    return False
            else:
                dct[10] += 1
                if dct[5] > 0:
                    dct[5] -= 1
                    continue
                else:
                    return False
        return True