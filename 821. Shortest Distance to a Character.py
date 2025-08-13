class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a,n=[],len(s)
        for i in range(n):
            if s[i]==c:
                a.append(i)
        answer=[]
        j=0
        for i in range(n):
            if s[i]==c:
                answer.append(0)
                j+=1
            elif i<a[0]:
                answer.append(a[0]-i)
            elif i>a[-1]:
                answer.append(i-a[-1])
            else:
                answer.append(min((a[j]-i),(i-a[j-1])))
        return answer
