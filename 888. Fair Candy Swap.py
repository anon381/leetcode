
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceTotal, bobTotal = 0, 0

        for candy in aliceSizes:
            aliceTotal += candy

        for candy in bobSizes:
            bobTotal += candy

        delta = (bobTotal - aliceTotal) // 2
        bobSet = set(bobSizes)

        for a in aliceSizes:
            b = a + delta
            if b in bobSet:
                return [a, b]
        
