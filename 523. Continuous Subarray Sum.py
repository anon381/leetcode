class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0:-1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %=k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >=2:
                return True
        return False




        
#in cpp
# class Solution {
# public:
#     bool checkSubarraySum(vector<int>& nums, int k) {
       
        
        
#         if(nums.size()<2)
#             return false;
        
        
        
#         mp[0]=-1;
        
#         int runningSum=0;
        
#         for(int i=0;i<nums.size();i++)
#         {
#             runningSum+=nums[i];
            
#             if(k!=0) 
#                 runningSum = runningSum%k;
            
#             if(mp.find(runningSum)!=mp.end())
#             {
                
#                 if(i-mp[runningSum]>1)
#                     return true;
#             }
#             else
#             {
                
#                 mp[runningSum]=i;
#             }
                    
#         }
        
#         return false;
        
#     }
# };
