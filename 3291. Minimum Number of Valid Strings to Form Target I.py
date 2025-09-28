class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        for word in words: 
            node = trie
            for ch in word: 
                node = node.setdefault(ch, {})
            node["#"] = word 
        n = len(target) 
        dp = [inf]*(n+1)
        dp[n] = 0 
        for i in range(n-1, -1, -1):
            node = trie
            for j in range(i, n):
                if target[j] in node: node = node[target[j]]
                else: break 
                dp[i] = min(dp[i], 1 + dp[j+1])
        return dp[0] if dp[0] < inf else -1 
