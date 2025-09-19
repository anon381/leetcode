class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp0 = [0] * n  
        dp1 = [0] * n  
        dp0[0] = arr[0]
        dp1[0] = -10**9  
        res = arr[0]
        for i in range(1, n):
            dp0[i] = max(dp0[i-1] + arr[i], arr[i])
            dp1[i] = max(dp1[i-1] + arr[i], dp0[i-1])
            res = max(res, max(dp0[i], dp1[i]))
        return res
