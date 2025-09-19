class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        seen = {}
        for i, x in enumerate(nums): 
            bkt = x//(t+1)
            if bkt in seen and i - seen[bkt][0] <= k: return True 
            if bkt-1 in seen and i - seen[bkt-1][0] <= k and abs(x - seen[bkt-1][1]) <= t: return True 
            if bkt+1 in seen and i - seen[bkt+1][0] <= k and abs(x - seen[bkt+1][1]) <= t: return True 
            seen[bkt] = (i, x) 
        return False 

#in cpp
# #include <unordered_map>
# #include <cmath>
# #include <vector>
# using namespace std;

# class Solution {
# public:
#     bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
#         if (t < 0) return false;

#         unordered_map<long long, pair<int, long long>> bucket;
#         long long w = (long long)t + 1; // bucket size

#         for (int i = 0; i < nums.size(); i++) {
#             long long x = (long long)nums[i];
#             long long bkt = x / w;
#             if (x < 0) bkt--; // handle negatives properly

#             // Check same bucket
#             if (bucket.count(bkt) && i - bucket[bkt].first <= k)
#                 return true;

#             // Check neighbor bucket
#             if (bucket.count(bkt - 1) && i - bucket[bkt - 1].first <= k &&
#                 abs(x - bucket[bkt - 1].second) <= t)
#                 return true;

#             if (bucket.count(bkt + 1) && i - bucket[bkt + 1].first <= k &&
#                 abs(x - bucket[bkt + 1].second) <= t)
#                 return true;

#             bucket[bkt] = {i, x};
#         }

#         return false;
#     }
# };

#in java
# import java.util.*;

# class Solution {
#     public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
#         if (t < 0) return false;

#         Map<Long, long[]> bucket = new HashMap<>();
#         long w = (long)t + 1; // bucket size

#         for (int i = 0; i < nums.length; i++) {
#             long x = nums[i];
#             long bkt = x / w;
#             if (x < 0) bkt--; // handle negatives

#             // Check same bucket
#             if (bucket.containsKey(bkt) && i - bucket.get(bkt)[0] <= k)
#                 return true;

#             // Check neighbors
#             if (bucket.containsKey(bkt - 1) && i - bucket.get(bkt - 1)[0] <= k &&
#                 Math.abs(x - bucket.get(bkt - 1)[1]) <= t)
#                 return true;

#             if (bucket.containsKey(bkt + 1) && i - bucket.get(bkt + 1)[0] <= k &&
#                 Math.abs(x - bucket.get(bkt + 1)[1]) <= t)
#                 return true;

#             bucket.put(bkt, new long[]{i, x});
#         }

#         return false;
#     }
# }
