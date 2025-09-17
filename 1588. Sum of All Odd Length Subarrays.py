  class Solution(object):
    def sumOddLengthSubarrays(self, A):
        n = len(A)
        res = 0
        for l in xrange(1, n + 1, 2):
            for i in xrange(n - l + 1):
                res += sum(A[i:i + l])
        return res
        
#in cpp
    # int sumOddLengthSubarrays(vector<int>& A) {
    #     int res = 0, n = A.size();
    #     for (int i = 0; i < n; ++i) {
    #         res += ((i + 1) * (n - i) + 1) / 2 * A[i];
    #     }
    #     return res;
    # }
#in java
