Complexity:

Time: O(1)

Space: O(1)
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5

#in cpp
class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        return (n == 1) ? 1.0 : 0.5;
    }
};

#in java
class Solution {
    public double nthPersonGetsNthSeat(int n) {
        return (n == 1) ? 1.0 : 0.5;
    }
}
