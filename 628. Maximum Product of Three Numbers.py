
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
## or 
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = 0
        if nums[0] < 0 and nums[1] < 0 :
            m = nums[0]*nums[1]*nums[n-1]
        return max(nums[n-3]*nums[n-2]*nums[n-1],m)
