class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:

        reverse = lambda num: int(bin(num)[-1:1:-1], 2)     # <--1)
        nums.sort(key = lambda x: (reverse(x), x))          # <--2)

        return nums
