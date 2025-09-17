class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        sum_of_weeks = 28*weeks + 7*(weeks*(weeks-1)//2)
        sum_of_days = days * (2*weeks + days + 1) // 2
        return sum_of_weeks + sum_of_days
