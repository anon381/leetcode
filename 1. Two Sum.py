class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

            #in cpp
            # unordered_map<int, int> pair_idx;
            # for (int i = 0; i < nums.size(); ++i) {
            #     if (pair_idx.count(target - nums[i])) {
            #         return {i, pair_idx[target - nums[i]]};
            #     }
            #     pair_idx[nums[i]] = i;
            # }


            #in java
            # import java.util.*;
            # class Solution {
            #     public int[] twoSum(int[] nums, int target) {
            #         Map<Integer, Integer> pairIdx = new HashMap<>();
            #         for (int i = 0; i < nums.length; i++) {
            #             if (pairIdx.containsKey(target - nums[i])) {
            #                 return new int[]{i, pairIdx.get(target - nums[i])};
            #             }
            #             pairIdx.put(nums[i], i);
            #         }
            #         throw new IllegalArgumentException("No two sum solution");
            #     }
            # }
        