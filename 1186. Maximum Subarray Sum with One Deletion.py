class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp0 = [0] * n  
        dp1 = [0] * n  

        dp0[0] = arr[0]
        dp1[0] = -10**9  
