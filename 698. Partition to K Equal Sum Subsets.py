class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(i, used, cursum):
            if used == DONE:
                return True
            
            for j in range(i, N):
                if used & (1 << j) > 0:
                    continue
                if j > 0 and used & (1 << j - 1) == 0 and nums[j] == nums[j - 1]:
                    continue
                
                if nums[j] + cursum < target:
                    if backtrack(j + 1, used | (1 << j), cursum + nums[j]):
                        return True
                elif nums[j] + cursum == target:
                    if backtrack(0, used | (1 << j), 0):
                        return True
                
                if i == 0:
                    break
            return False

        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        nums.sort(reverse=True)
        N = len(nums)
        DONE = (1 << N) - 1
        print(nums)
        return backtrack(0, 0, 0)


#in cpp
