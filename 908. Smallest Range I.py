class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:

        M, m = max(A), min(A)
        diff, extension = M - m, 2*K
        
        if diff <= extension:
            return 0
        
        else:
            return diff - extension

# in cpp
# class Solution {
# public:
#     int smallestRangeI(vector<int>& nums, int k) {
#         int maxi{INT_MIN}, mini{INT_MAX};
#         for(int i=0;i<nums.size();i++){
#             maxi = max(maxi, nums[i]);
#             mini = min(mini, nums[i]);
#         }
#     return (maxi-mini)-(2*k)>0?(maxi-mini)-(2*k):0;
#     }
# };
