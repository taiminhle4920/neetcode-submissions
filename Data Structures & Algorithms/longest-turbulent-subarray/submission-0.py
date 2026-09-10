class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxT = 1
        cur = 1
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                if i > 1 and arr[i-1] > arr[i-2]:
                    cur = 2
                else:
                    cur += 1
            elif arr[i] < arr[i-1]:
                if i > 1 and arr[i-1]< arr[i-2]:
                    cur = 2
                else:
                    cur += 1
                    
            else:
                cur = 1

            maxT = max(maxT, cur)
        return maxT