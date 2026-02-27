class Solution(object):
    def mostVisited(self, n, A):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        return range(A[0], A[-1] + 1) or range(1, A[-1] + 1) + range(A[0], n + 1)
