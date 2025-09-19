class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        num = 0
        
        for n in nums:
            num = (num * 2 + n) % 5
            res.append(num == 0)
            
        return res
#in cpp
# class Solution {
# public:
#     vector<bool> prefixesDivBy5(vector<int>& nums) {
        
#         vector<bool> res;
#         int num;
        
#         for(int i = 0; i < nums.size(); ++i)
#         {
#             num = (num * 2 + nums[i]) % 5;
#             res.push_back(num == 0);
#         }
        
#         return res;
#     }
# };
