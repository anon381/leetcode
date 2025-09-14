class Solution:
    def countOrders(self, n: int) -> int:
        cap = 10**9 + 7
        pickup_permutation = math.factorial(n) % cap
        delivery_permutation = reduce(mul, range(1, 2*n, 2), 1) % cap
        return pickup_permutation * delivery_permutation % cap


#in cpp
# int countOrders(int n) {
#     long long res = 1, cap = 1000000007;
#     for (int i=1; i<n+1; ++i) res = res * i % cap;
#     for (int i=1; i<2*n; i+=2) res = res * i % cap;
#     return res;
# }
