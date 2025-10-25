class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        y = sum(nums)
        nums.reverse()
        a,count = 0,0
        for i in nums:
            if a+i > y -(a+i):
                break
            else:
                a+=i
            count+=1
        return(nums[0:count+1])



