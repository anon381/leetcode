class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        def bucket_sorted(arr):
            c = collections.Counter(arr)
            return [x for i in range(10) if i in c for x in [i]*c[i]]
        
        d = collections.defaultdict(list)
        for n in digits:
            d[n%3] += n,
        res, short, long = d[0], *sorted((d[1], d[2]), key=len)
        short, long = bucket_sorted(short), bucket_sorted(long)
        
        if (len(long) - len(short)) % 3 > abs((len(long) % 3) - (len(short) % 3)):
            short, long = (short, long) if len(short)%3 < len(long)%3 else (long, short)
            res += short + long[abs(len(short)%3 - len(long)%3):]
        else:
            res += short + long[(len(long)-len(short))%3:]
            
        res = bucket_sorted(res)[::-1]
        return '0' if res and not res[0] else ''.join(map(str, res))

# C++ version of the above Python code:
#
# #include <vector>
# #include <string>
# #include <algorithm>
# using namespace std;
# class Solution {
# public:
#     string largestMultipleOfThree(vector<int>& digits) {
#         sort(digits.rbegin(), digits.rend());
#         int sum = 0;
#         vector<int> mod[3];
#         for (int d : digits) {
#             sum += d;
#             mod[d % 3].push_back(d);
#         }
#         int r = sum % 3;
#         if (r) {
#             if (!mod[r].empty()) mod[r].pop_back();
#             else if (mod[3 - r].size() >= 2) mod[3 - r].pop_back(), mod[3 - r].pop_back();
#             else return "";
#         }
#         vector<int> res;
#         for (int i = 0; i < 3; ++i) res.insert(res.end(), mod[i].begin(), mod[i].end());
#         sort(res.rbegin(), res.rend());
#         if (res.empty() || res[0] == 0) return "0";
#         string ans;
#         for (int d : res) ans += to_string(d);
#         return ans;
#     }
# };