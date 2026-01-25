class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        start, second = heapq.nsmallest(2, arr)
        return set(islice(count(start, second - start), len(arr))) == set(arr)
