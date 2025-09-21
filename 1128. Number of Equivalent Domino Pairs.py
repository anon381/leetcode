Complexity
Time complexity = O(n)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = [0] * 100
        res = 0
        for a, b in dominoes:
            val = a * 10 + b if a < b else b * 10 + a
            res += count[val]
            count[val] += 1
        return res
