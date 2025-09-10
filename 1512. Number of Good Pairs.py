class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

        #cpp version of the above python code:
        #include <vector>
        #using namespace std;
        #class Solution {
        #public:
        #    int numIdenticalPairs(vector<int>& nums) {
        #        int count = 0;
        #        for (int i = 0; i < nums.size(); i++) {
        #            for (int j = i + 1; j < nums.size(); j++) {
        #                if (nums[i] == nums[j]) {
        #                    count++;
        #                }
        #            }
        #        }
        #        return count;
        #    }
        #};