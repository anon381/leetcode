class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67,
          71, 73, 79, 83, 89, 97]
        primes = [x for x in range(2, n + 1) if x in p]
        return (factorial(len(primes)) * factorial(n - len(primes))) % int(1e9 + 7)



#c++ version 
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     int numPrimeArrangements(int n) {
#         const int MOD = 1e9 + 7;

#         // List of primes up to 100
#         vector<int> p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#                          31, 37, 41, 43, 47, 53, 59, 61, 67,
#                          71, 73, 79, 83, 89, 97};

#         // Count how many primes ≤ n
#         int primeCount = 0;
#         for (int x : p) {
#             if (x <= n) primeCount++;
#         }

#         // Function to compute factorial % MOD
#         auto factorial = [&](int k) {
#             long long res = 1;
#             for (int i = 2; i <= k; i++) {
#                 res = (res * i) % MOD;
#             }
#             return res;
#         };

#         long long ans = (factorial(primeCount) * factorial(n - primeCount)) % MOD;
#         return (int)ans;
#     }
# };

