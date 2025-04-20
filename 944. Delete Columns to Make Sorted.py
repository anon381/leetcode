class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return len([True for col in zip(*A) if sorted(col) != list(col)])