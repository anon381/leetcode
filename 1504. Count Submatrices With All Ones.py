class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        h = [0] * c
        ans = 0
        for i in range(r):
            for j in range(c):
                h[j] = h[j] + 1 if mat[i][j] else 0
            sumv, st = [0] * c, []
            for j in range(c):
                while st and h[st[-1]] >= h[j]:
                    st.pop()
                if st:
                    p = st[-1]
                    sumv[j] = sumv[p] + h[j] * (j - p)
                else:
                    sumv[j] = h[j] * (j + 1)
                st.append(j)
                ans += sumv[j]
        return ans
## or a bit changed approach 

  class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c=len(mat), len(mat[0])
        ans=0
        for i, h in enumerate(mat):
            st=[]
            cnt=[0]*c
            for j in range(c):
                if i>0 and h[j]>0:
                    h[j]+=mat[i-1][j]
                while st and h[st[-1]]>h[j]:
                    st.pop()
                left=st[-1] if st else -1
                cnt[j]=h[j]*(j-left)
                if st: cnt[j]+=cnt[left]
                ans+=cnt[j]
                st.append(j)
        return ans
        
