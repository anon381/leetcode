class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0
        start = 0

        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res.append(s[start + 1:i])
                start = i + 1
        return ''.join(res)



#in cpp
# class Solution {
# public:
#     string removeOuterParentheses(string s) {
#         string res;
#         int balance = 0, start = 0;
#         for (int i = 0; i < s.length(); ++i) {
#             if (s[i] == '(') balance++;
#             else balance--;
#             if (balance == 0) {
#                 res += s.substr(start + 1, i - start - 1);
#                 start = i + 1;
#             }
#         }
#         return res;
#     }
# };


#in java
# class Solution {
#     public String removeOuterParentheses(String s) {
#         int sum = 0, start = 0, end = 0;
#         StringBuilder res = new StringBuilder();

#         while (end < s.length()) {
#             if (s.charAt(end) == '(') sum++;
#             else sum--;

#             if (sum == 0) {
#                 res.append(s.substring(start + 1, end)); // exclude outer
#                 start = end + 1;
#             }
#             end++;
#         }
#         return res.toString();
#     }
# }
