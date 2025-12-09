
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        memo, duplets = {}, {}
        res = 0
        MOD = 10 ** 9 + 7

        for number in nums:
            if number in duplets:
                res = (res + duplets[number]) % MOD

            twon = number * 2
            if twon in memo:
                duplets[twon] = (duplets.get(twon, 0) + memo[twon]) % MOD
            
            memo[number] = memo.get(number, 0) + 1

        return res
