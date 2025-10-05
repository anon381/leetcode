
import math

def twoEggDrop(n: int) -> int:
    return math.ceil((-1 + math.sqrt(1 + 8*n)) / 2)


#in cpp
#include <cmath>
using namespace std;

class Solution {
public:
    int twoEggDrop(int n) {
        // smallest k such that k*(k+1)/2 >= n
        return ceil((-1 + sqrt(1 + 8.0 * n)) / 2);
    }
};
