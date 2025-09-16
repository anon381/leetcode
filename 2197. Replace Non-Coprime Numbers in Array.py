from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = (stack.pop() * num) // g
            stack.append(num)
        return stack



#in cpp
# class Solution {
# public:
#     vector<int> replaceNonCoprimes(vector<int>& nums) {
#         vector<int> stack;
#         for (int num : nums) {
#             while (!stack.empty()) {
#                 int top = stack.back();
#                 int g = gcd(top, num);
#                 if (g == 1) {
#                     break;
#                 }
#                 stack.pop_back();
#                 // compute LCM
#                 long long merged = (long long)top / g * num;
#                 num = (int)merged;
#             }
#             stack.push_back(num);
#         }
#         return stack;
#     }
# private:
#     int gcd(int a, int b) {
#         return b == 0 ? a : gcd(b, a % b);
#     }
# };



# in java
# class Solution {
#     public List<Integer> replaceNonCoprimes(int[] nums) {
#         List<Integer> stack = new ArrayList<>();       
#         for (int num : nums) {
#             while (!stack.isEmpty()) {
#                 int top = stack.get(stack.size() - 1);
#                 int g = gcd(top, num);
#                 if (g == 1) {
#                     break;
#                 }
#                 // merge top with current num (via LCM)
#                 stack.remove(stack.size() - 1);
#                 num = (top / g) * num;  // safer LCM
#             }
#             stack.add(num);
#         }
#         return stack;
#     }
#     private int gcd(int a, int b) {
#         if (b == 0) return a;
#         return gcd(b, a % b);
#     }
# }
