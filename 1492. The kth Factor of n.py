class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count =0
        for i in range(1,1+n):
            if n%i==0:
                count+= 1
                if count == k: return i
        return -1
