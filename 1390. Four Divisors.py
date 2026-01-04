class Solution:
    def factors(self, n: int) -> int:
        total = 0
        c = 0
        i = 2
        while i * i <= n:
            if n % i == 0:
                j = n // i
                if j == i or c > 0:
                    return 0
                total += i + j
                c += 1
            i += 1

        if c == 0:
            return 0
        return 1 + total + n

    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += self.factors(num)
        return total_sum
