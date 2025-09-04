class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(x - z), abs(y - z)
        return (a != b) << (a > b)
