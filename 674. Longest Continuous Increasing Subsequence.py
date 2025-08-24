
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                prev = max(count, prev)
                count = 1
        return max(prev, count)
