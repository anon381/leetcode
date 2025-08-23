class BIT:
    def __init__(self, N):
        self.stree = [0] * (N + 1)

    def increase(self, i, x):
        while i < len(self.stree):
            self.stree[i] += x
            i |= (i + 1)

    def total(self, i):
        sum = 0
        while i >= 0:
            sum += self.stree[i]
            i = (i & (i + 1)) - 1
        return sum

class NumArray:
    def __init__(self, nums):
        self.bit = BIT(len(nums))
        self.nums = nums
        for i in range(len(nums)):
            self.bit.increase(i + 1, nums[i])

    def update(self, index, val):
        delta = val - self.nums[index]
        self.bit.increase(index + 1, delta)
        self.nums[index] += delta

    def sumRange(self, left, right):
        return self.bit.total(right + 1) - self.bit.total(left)
