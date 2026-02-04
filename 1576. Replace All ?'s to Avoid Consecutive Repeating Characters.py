class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?": 
                for c in "abc": 
                    if (i == 0 or s[i-1] != c) and (i+1 == len(s) or s[i+1] != c): 
                        s[i] = c
                        break 
        return "".join(s)
