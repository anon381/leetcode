from collections import deque
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
      if not matrix or not matrix[0]:
            return False                
        expected = deque(matrix[0])
        for row_i in range(1, len(matrix)):
            row = matrix[row_i]
            expected.pop()
            expected.appendleft(row[0])
            for col_i in range(1, len(row)):
                if row[col_i] != expected[col_i]:
                    return False
        return True
