class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        one = []
        two = []
        three = []
        for i in digits:
            if i % 3 == 1:
                one.append(str(i))
            elif i % 3 == 2:
                two.append(str(i))
            else:
                three.append(str(i))
        one.sort()
        two.sort()
        one = one[::-1]
        two = two[::-1]
        if sum(digits) % 3 == 1:
            try:
                one.pop()
            except:
                two.pop()
                two.pop()
        elif sum(digits) % 3 == 2:
            try:
                two.pop()
            except:
                one.pop()
                one.pop()
        ans = "".join(one)
        ans += "".join(two)
        ans += "".join(three)
        
        if ans == "":
            return ""
        if ans[0] == "0":
            return "0"
        ans = "".join(sorted(ans))[::-1]
        return ans



# c++ version
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     string largestMultipleOfThree(vector<int>& digits) {
#         vector<int> one, two, three;

#         for (int d : digits) {
#             if (d % 3 == 1) one.push_back(d);
#             else if (d % 3 == 2) two.push_back(d);
#             else three.push_back(d);
#         }

#         sort(one.begin(), one.end(), greater<int>());
#         sort(two.begin(), two.end(), greater<int>());
#         sort(three.begin(), three.end(), greater<int>());

#         int total = accumulate(digits.begin(), digits.end(), 0);

#         if (total % 3 == 1) {
#             if (!one.empty()) {
#                 one.pop_back();
#             } else if (two.size() >= 2) {
#                 two.pop_back();
#                 two.pop_back();
#             } else {
#                 return "";
#             }
#         } else if (total % 3 == 2) {
#             if (!two.empty()) {
#                 two.pop_back();
#             } else if (one.size() >= 2) {
#                 one.pop_back();
#                 one.pop_back();
#             } else {
#                 return "";
#             }
#         }

#         vector<int> res;
#         res.insert(res.end(), one.begin(), one.end());
#         res.insert(res.end(), two.begin(), two.end());
#         res.insert(res.end(), three.begin(), three.end());

#         if (res.empty()) return "";

#         sort(res.begin(), res.end(), greater<int>());

#         if (res[0] == 0) return "0";  // only zeros remain

#         string ans;
#         for (int d : res) ans.push_back(d + '0');
#         return ans;
#     }
# };


# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public String largestMultipleOfThree(int[] digits) {
#         Arrays.sort(digits);
#         int sum = 0;
#         List<Integer>[] mod = new List[3];
#         for (int i = 0; i < 3; ++i) mod[i] = new ArrayList<>();
#         for (int d : digits) {
#             sum += d;
#             mod[d % 3].add(d);
#         }
#         int r = sum % 3;
#         if (r != 0) {
#             if (!mod[r].isEmpty()) mod[r].remove(0);
#             else if (mod[3 - r].size() >= 2) { mod[3 - r].remove(0); mod[3 - r].remove(0); }
#             else return "";
#         }
#         List<Integer> res = new ArrayList<>();
#         for (int i = 0; i < 3; ++i) res.addAll(mod[i]);
#         res.sort(Collections.reverseOrder());
#         if (res.isEmpty() || res.get(0) == 0) return "0";
#         StringBuilder sb = new StringBuilder();
#         for (int d : res) sb.append(d);
#         return sb.toString();
#     }
# }
#
