class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        currsum = sum(nums[:k])
        maxval = currsum / k
        for i in range(k, len(nums)):
            currsum -= nums[i-k]
            currsum += nums[i]
            if currsum / k > maxval:
                maxval = currsum/k
        return maxval
