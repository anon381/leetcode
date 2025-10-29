
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1<<(1+int(log2(n))))-1
