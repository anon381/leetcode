class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        c = 0
        while n1 and n2:
            c += n1 // n2
            n1 %= n2
            n1, n2 = n2, n1
        return c
