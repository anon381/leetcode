# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(n), for the hash map storing indices
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}  # Dictionary to store previously seen numbers and their indices

        for i, num in enumerate(nums):  # Loop through each number with its index
            if target - num in pair_idx:  # Check if the complement exists in the dictionary
                return [i, pair_idx[target - num]]  # If found, return current index and index of complement
            pair_idx[num] = i  # Otherwise, store the current number and its index in the dictionary

# Function Description:
# This function finds two distinct indices in the list 'nums' such that the numbers at those indices add up to the given 'target'.
# It uses a hash map to store previously seen numbers and their indices, allowing for efficient lookup of the complement (target - num).
# When a valid pair is found, their indices are returned as a list.

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
