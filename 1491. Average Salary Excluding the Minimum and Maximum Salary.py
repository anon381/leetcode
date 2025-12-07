class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        middle = salary[1:-1]
        return sum(middle) / len(middle)
