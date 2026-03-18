class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            for start, end in ranges:
                if start <= x <= end:
                    break
            else:
                return False
        
        return True
        
        1893. Check if All the Integers in a Range Are Covered
