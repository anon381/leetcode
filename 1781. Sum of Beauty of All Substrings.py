Complexity
Time complexity: O(n ^ 2)

class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i, len(s)):
                freq[s[j]] += 1
                total_beauty += max(freq.values()) - min(freq.values())
        return total_beauty
