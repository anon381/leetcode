
from bisect import bisect_right
from typing import List

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        res = []
        
        for b in B:
            # find the smallest element in A greater than b
            idx = bisect_right(A, b)
            if idx < len(A):
                # use that element
                res.append(A[idx])
                A.pop(idx)
            else:
                # no element greater than b → use the smallest available
                res.append(A[0])
                A.pop(0)
        
        return res

#in cpp
class Solution {
public:
       vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        multiset<int> s(begin(A), end(A));
        for (int i = 0; i < B.size(); ++i) {
            auto it = *s.rbegin() > B[i] ? s.upper_bound(B[i]) : s.begin();
            A[i] = *it;
            s.erase(it);
        }
        return A;
    }
};
