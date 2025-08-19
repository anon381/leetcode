
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_x, min_y = m, n
        for a, b in ops:
            if min_x > a: min_x = a
            if min_y > b: min_y = b
        return min_x * min_y

## or 
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        for i in range(len(ops)):
            min_row=min(min_row, ops[i][0])
            min_col=min(min_col, ops[i][1])
        return min_row*min_col
