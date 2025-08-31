class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        is_inc = True
        is_dec = True

        for i in range(1, n):
            if not is_inc and not is_dec:
                return False

            if nums[i] < nums[i-1]:
                is_inc = False
            if nums[i] > nums[i-1]:
                is_dec = False

        return is_inc or is_dec



#in cpp
# class Solution {
# public:
#     bool isMonotonic(vector<int>& nums) {
#         int n = nums.size();
#         if (n == 1) return true;

#         bool isInc = true;
#         bool isDec = true;

#         for (int i = 1; i < n; i++) {
#             if (!isInc && !isDec) {
#                 return false;
#             }

#             if (nums[i] < nums[i - 1]) {
#                 isInc = false;
#             }
#             if (nums[i] > nums[i - 1]) {
#                 isDec = false;
#             }
#         }




#in java 
# class Solution {
#     public boolean isMonotonic(int[] nums) {
#         int n = nums.length;
#         if (n == 1) return true;
#         boolean isInc = true;
#         boolean isDec = true;
#         for (int i = 1; i < n; i++) {
#             if (!isInc && !isDec) {
#                 return false;
#             }
#             if (nums[i] < nums[i - 1]) {
#                 isInc = false;
#             }
#             if (nums[i] > nums[i - 1]) {
#                 isDec = false;
#             }
#         }
#         return isInc || isDec;        
#     }
# }
#         return isInc || isDec;        
#     }
# };
