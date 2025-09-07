class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        
      
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    m = min(len(words[i]), len(words[j]))
                    for k in range(m, 0, -1):
                        if words[i].endswith(words[j][:k]):
                            overlap[i][j] = k
                            break
        
        dp = [[""]*n for _ in range(1<<n)]
        for i in range(n):
            dp[1<<i][i] = words[i]
        for mask in range(1<<n):
            for j in range(n):
                if not (mask & (1<<j)):
                    continue
                prev_mask = mask ^ (1<<j)
                if prev_mask == 0:
                    continue
                for i in range(n):
                    if not (prev_mask & (1<<i)):
                        continue
                    candidate = dp[prev_mask][i] + words[j][overlap[i][j]:]
                    if dp[mask][j] == "" or len(candidate) < len(dp[mask][j]):
                        dp[mask][j] = candidate
        
        full_mask = (1<<n) - 1
        ans = None
        for i in range(n):
            if ans is None or len(dp[full_mask][i]) < len(ans):
                ans = dp[full_mask][i]
        return ans
