class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        res = []
        count = 0
        for i in nums:
            if i == 0:
                count += 1
                continue
            val *= i
        for i in nums:
            if i == 0 and count == 1:

                res.append(val)
            elif i == 0 and count > 1:

                res.append(0)
            elif i != 0 and count > 0:
                res.append(0)
            else:
                res.append(val//i)
        return res