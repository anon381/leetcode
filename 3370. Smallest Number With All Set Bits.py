# complexity
# Time complexity:
# O(1)∼O(logn)

# Space complexity:
# O(1)
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1<<(1+int(log2(n))))-1
#in cpp
class Solution {
public:
    int smallestNumber(unsigned n) {
        int x=1023, prev;
        for(; x>=n; x>>=1)
            prev=x;
        return prev;
    }
};
