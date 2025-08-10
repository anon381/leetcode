class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        n=len(s)//2
        lp=s[:n]
        kp=s[n:]
        f,e=0,len(s)-1
        while f<e:
            if s[f]!=s[e]:
                if (s[:f]+s[f+1:]==(s[:f]+s[f+1:])[::-1]) or s[:e]+s[e+1:]==(s[:e]+s[e+1:])[::-1]:
                    return True
                else:
                    return False
            f+=1
            e-=1
        return False
