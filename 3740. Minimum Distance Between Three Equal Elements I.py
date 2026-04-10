class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_result = 1000
        y = set(nums)
        for k in y:
            indices = [i for i, x in enumerate(nums) if x == k]
            if len(indices) >2:
                for i in range(len(indices) -2):
                    answer = abs(indices[i] - indices[i+1]) + abs(indices[i+1] - indices[i+2])+abs(indices[i+2] - indices[i])
                    min_result = min(answer, min_result) 
        if min_result != 1000:
            return min_result
        else:
            return -1
