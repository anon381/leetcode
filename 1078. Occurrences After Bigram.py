class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        words = text.split(' ')
        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                ans.append(words[i])
        return ans        
