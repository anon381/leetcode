class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        elif num % 10 == 0:
            return False
        else:
            return True
