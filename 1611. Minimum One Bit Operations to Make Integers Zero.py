class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res
#in cpp
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int res = 0;
        while (n) {
            res ^= n;
            n >>= 1;
        }
        return res;
    }
};
#in java
class Solution {
    public int minimumOneBitOperations(int n) {
        int res = 0;
        while (n > 0) {
            res ^= n;
            n >>= 1;
        }
        return res;
    }
}
