class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        for i in range(n):
            nums[i] = start+2*i
        
        count = nums[0]
        for j in range (1,n):
            count ^= nums[j]
        return count
