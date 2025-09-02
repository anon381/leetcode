class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        mod=10**9+7
        d={}
        for i in range(1,n+1):
            char=s[i-1]
            
            dp[i]=(2*dp[i-1])%mod
            if char in d:
                idx=d[char]
                dp[i]=((dp[i]-dp[idx-1])+mod)%mod
            d[char]=i
        return (dp[n]-1)%mod



#in cpp
