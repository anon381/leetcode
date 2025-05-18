class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)

         d = {}

        for i, num in enumerate(temp):
            if num not in d:      
                d[num] = i       

        ret = []
        for i in nums:
            ret.append(d[i])      

        return ret

# C++ version of the above Python code:
#
# #include <vector>
# #include <algorithm>
# #include <unordered_map>
# using namespace std;
# class Solution {
# public:
#     vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
#         vector<int> temp = nums;
#         sort(temp.begin(), temp.end());
#         unordered_map<int, int> d;
#         for (int i = 0; i < temp.size(); ++i) {
#             if (d.find(temp[i]) == d.end()) {
#                 d[temp[i]] = i;
#             }
#         }
#         vector<int> ret;
#         for (int num : nums) {
#             ret.push_back(d[num]);
#         }
#         return ret;
#     }
# };
#