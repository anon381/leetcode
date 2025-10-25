class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        y = sum(nums)
        nums.reverse()
        a,count = 0,0
        for i in nums:
            if a+i > y -(a+i):
                break
            else:
                a+=i
            count+=1
        return(nums[0:count+1])



#in cpp

class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int total = accumulate(nums.begin(), nums.end(), 0);
        reverse(nums.begin(), nums.end());
        
        int curr = 0;
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            curr += nums[i];
            if (curr > total - curr) {
                count = i;
                break;
            }
        }
        return vector<int>(nums.begin(), nums.begin() + count + 1);
    }
};
