# Complexity

# Time: O(n log n) (merge sort + counting).

# Space: O(n) (prefix sums + recursion stack).

class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid, hi)

            j = k = mid
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k

            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return merge_sort(0, len(prefix))

#in cpp
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     int countRangeSum(vector<int>& nums, int lower, int upper) {
#         int n = nums.size();
#         vector<long long> prefix(n + 1, 0);
#         for (int i = 0; i < n; i++) {
#             prefix[i + 1] = prefix[i] + nums[i];
#         }
#         return mergeSort(prefix, 0, n + 1, lower, upper);
#     }

# private:
#     int mergeSort(vector<long long>& prefix, int lo, int hi, int lower, int upper) {
#         if (hi - lo <= 1) return 0;
#         int mid = (lo + hi) / 2;
#         int count = mergeSort(prefix, lo, mid, lower, upper) +
#                     mergeSort(prefix, mid, hi, lower, upper);

#         int j = mid, k = mid;
#         for (int i = lo; i < mid; i++) {
#             while (k < hi && prefix[k] - prefix[i] < lower) k++;
#             while (j < hi && prefix[j] - prefix[i] <= upper) j++;
#             count += j - k;
#         }
#         inplace_merge(prefix.begin() + lo, prefix.begin() + mid, prefix.begin() + hi);
#         return count;
#     }
# };




#in java
