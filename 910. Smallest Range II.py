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
    public int smallestRangeII(int[] A, int K) {
        Arrays.sort(A);
        int n = A.length, mx = A[n - 1], mn = A[0], res = mx - mn;
        for (int i = 0; i < n - 1; ++i) {
            mx = Math.max(mx, A[i] + 2 * K);
            mn = Math.min(A[i + 1], A[0] + 2 * K);
            res = Math.min(res, mx - mn);
        }
        return res;
    }


#in cpp
    int smallestRangeII(vector<int> A, int K) {
        sort(A.begin(), A.end());
        int n = A.size(), mx = A[n - 1], mn = A[0], res = mx - mn;
        for (int i = 0; i < n - 1; ++i) {
            mx = max(mx, A[i] + 2 * K);
            mn = min(A[i + 1], A[0] + 2 * K);
            res = min(res, mx - mn);
        }
        return res;
    }
