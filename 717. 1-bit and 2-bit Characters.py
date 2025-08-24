
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        idx = 0
        n = len(bits)
        while idx < n - 1:
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1
        return idx == n - 1
