class Solution:
  def removeDuplicates(self, S):
    return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, S)

# or

class Solution:
    def removeDuplicates(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)


#in cpp
# class Solution {
# public:
#         string removeDuplicates(string S) {
#         string res = "";
#         for (char& c : S)
#             if (res.size() && c == res.back())
#                 res.pop_back();
#             else
#                 res.push_back(c);
#         return res;
#     }
# };


#in java
# class Solution {
#         public String removeDuplicates(String S) {
#         StringBuilder sb = new StringBuilder();
#         for (char c : S.toCharArray()) {
#             int size = sb.length();
#             if (size > 0 && sb.charAt(size - 1) == c) {
#                 sb.deleteCharAt(size - 1);
#             } else {
#                 sb.append(c);
#             }
#         }
#         return sb.toString();
#     }
# }
