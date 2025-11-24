class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        res = 0

        for ch in s:
            if ch == 'L':
                countL += 1
            else:
                countR += 1

            if countL == countR:
                res += 1

        return res
