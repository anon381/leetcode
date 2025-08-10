class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        r = 0
        for c in s:
            d[c] = d.get(c, 0) + 1
        for v in d.values():
            r += v if v % 2 == 0 else v - 1
        return r + 1 if r < len(s) else r
