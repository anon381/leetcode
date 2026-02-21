class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num

            while num > 0:
                digit_sum += num % 10
                num //= 10

        return element_sum - digit_sum
