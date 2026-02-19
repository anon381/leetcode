
class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        for i in range(2, n // 2 + 1):
            cnt += n % i == 0
            if cnt > 1:
                return False
        return cnt == 1
