class Solution:
    def getMaxSubarraySum(self,arr,size):
        n = len(arr)
        if n < size: return 0
        best = tmp = sum(arr[:size])
        for i in range(1,n-size+1):
            tmp = tmp + arr[i+size-1] - arr[i-1]
            if tmp > best:best = tmp
        return best
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        summ = sum(nums[:firstLen])
        ans = summ  + self.getMaxSubarraySum(nums[firstLen:],secondLen)   
        for i in range(1,n-firstLen+1):
            summ = summ + nums[i+firstLen-1] - nums[i-1]
            a = self.getMaxSubarraySum(nums[:i],secondLen)
            b = self.getMaxSubarraySum(nums[i+firstLen:],secondLen)
            m = a if a > b else b
            if summ + m > ans: ans = summ + m
        return ans
