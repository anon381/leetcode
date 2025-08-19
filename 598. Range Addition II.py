
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_x, min_y = m, n
        for a, b in ops:
            if min_x > a: min_x = a
            if min_y > b: min_y = b
        return min_x * min_y
