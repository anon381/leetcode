class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67,
          71, 73, 79, 83, 89, 97]
        primes = [x for x in range(2, n + 1) if x in p]
        return (factorial(len(primes)) * factorial(n - len(primes))) % int(1e9 + 7)
