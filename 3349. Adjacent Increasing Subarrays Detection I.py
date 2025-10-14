class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        knew = k - 1
        if knew == 0:
            return True
        for j in range(k + 1, len(nums)):
            if nums[j] > nums[j - 1] and nums[j - k] > nums[j - k - 1]:
                knew -= 1
            else:
                knew = k - 1
            if knew == 0:
                return True
        return False

#in cpp
class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int knew = k-1;
        if(knew == 0)return true;
        for(int j=k+1;j<nums.size();j++){
            if(nums[j] > nums[j-1] && nums[j-k] > nums[j-k-1])knew--;
            else knew = k - 1;
            if(knew == 0)return true;
        }
        return false;
    }
};
