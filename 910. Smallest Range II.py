class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            big = max(A[-1], A[i] + 2 * K)
            small = min(A[i + 1], A[0] + 2 * K)
            res = min(res, big - small)
        return res

#in java
