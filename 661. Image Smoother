class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        
        def average_value(r, c):
            total, count = 0, 0

            top = max(0, r - 1)
            bottom = min(rows, r + 2)
            left = max(0, c - 1)
            right = min(cols, c + 2)

            for row in range(top, bottom):
                for col in range(left, right):
                    total += img[row][col]
                    count += 1

            return total // count

        return [[average_value(r, c) for c in range(cols)] for r in range(rows)]
