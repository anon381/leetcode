class Solution:
    def makeGood(self, s: str) -> str:
        n=len(s)
        ans=[]
        for c in s:
            if ans and abs(ord(ans[-1])-ord(c))==32:
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)
