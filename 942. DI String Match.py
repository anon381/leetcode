# Final Complexity

# Time Complexity = O(n)

# Space Complexity = O(n)

class Solution:
    def diStringMatch(self, S):
        left = right = 0
        res = [0]
        for i in S:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [i - left for i in res]        


#in cpp
# class Solution {
# public:
#           vector<int> diStringMatch(string S) {
#         int left = count(S.begin(), S.end(), 'D'), right = left;
#         vector<int> res = {left};
#         for (char &c : S)
#             res.push_back(c == 'I' ? ++right : --left);
#         return res;
#     }
# };


#in java
# class Solution {
#         public int[] diStringMatch(String S) {
#         int n = S.length(), left = 0, right = n;
#         int[] res = new int[n + 1];
#         for (int i = 0; i < n; ++i)
#             res[i] = S.charAt(i) == 'I' ? left++ : right--;
#         res[n] = left;
#         return res;
#     }
# }
