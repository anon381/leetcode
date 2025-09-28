
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:

        nums = [abs(x) for x in nums]
        nums.sort()
        
        n, left = len(nums), 0
        ans = (n - 1) * n // 2
        
        for rght, num in enumerate(nums):
            while left < rght and num > 2 * nums[left]:
                left+= 1
            ans-= left
            
        return ans
