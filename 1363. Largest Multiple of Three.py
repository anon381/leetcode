
# Function Description:
# This function finds the largest number that can be formed from the given list of digits
# such that the number is a multiple of three. It does so by grouping digits based on their
# remainder when divided by three, sorting them, and removing the minimal number of digits
# to ensure the sum of the digits is divisible by three. The result is returned as a string.

# Time Complexity: O(n log n), where n is the number of digits (due to sorting)
# Space Complexity: O(n)

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        one = []  # Digits with remainder 1 when divided by 3
        two = []  # Digits with remainder 2 when divided by 3
        three = []  # Digits divisible by 3
        for i in digits:  # Loop through each digit
            if i % 3 == 1:  # If digit mod 3 is 1
                one.append(str(i))  # Add to 'one' list
            elif i % 3 == 2:  # If digit mod 3 is 2
                two.append(str(i))  # Add to 'two' list
            else:  # If digit mod 3 is 0
                three.append(str(i))  # Add to 'three' list
        one.sort()  # Sort 'one' list in ascending order
        two.sort()  # Sort 'two' list in ascending order
        one = one[::-1]  # Reverse 'one' for descending order
        two = two[::-1]  # Reverse 'two' for descending order
        # Adjust lists so sum of digits is divisible by 3
        if sum(digits) % 3 == 1:  # If total sum mod 3 is 1
            try:
                one.pop()  # Remove one smallest 'one' digit
            except:  # If no 'one' digit, remove two smallest 'two' digits
                two.pop()
                two.pop()
        elif sum(digits) % 3 == 2:  # If total sum mod 3 is 2
            try:
                two.pop()  # Remove one smallest 'two' digit
            except:  # If no 'two' digit, remove two smallest 'one' digits
                one.pop()
                one.pop()
        ans = "".join(one)  # Concatenate 'one' digits
        ans += "".join(two)  # Concatenate 'two' digits
        ans += "".join(three)  # Concatenate 'three' digits
        # Handle edge cases
        if ans == "":  # If result is empty
            return ""  # Return empty string
        if ans[0] == "0":  # If result starts with zero
            return "0"  # Return "0"
        ans = "".join(sorted(ans))[::-1]  # Sort digits in descending order
        return ans  # Return final answer



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
