class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        i=0
        for cookie in s:
            if cookie>=g[i]:
                i+=1
                if i==len(g):
                    break
        return i
