class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = reduce(lambda x, y: x & y, map(Counter, words))
        return list(common_counts.elements())


#in cpp


# class Solution {
# public:
#     vector<string> commonChars(vector<string>& words) {
#         // Initialize counts with large number (each char freq will be minimized)
#         vector<int> common(26, INT_MAX);

#         for (auto& word : words) {
#             vector<int> freq(26, 0);
#             for (char c : word) {
#                 freq[c - 'a']++;
#             }
#             for (int i = 0; i < 26; i++) {
#                 common[i] = min(common[i], freq[i]);
#             }
#         }

#         vector<string> result;
#         for (int i = 0; i < 26; i++) {
#             while (common[i]-- > 0) {
#                 result.push_back(string(1, 'a' + i));
#             }
#         }
#         return result;
#     }
# };


#in java
# class Solution {
#    public List<String> commonChars(String[] A) {
#         int[] last = count(A[0]);
#         for (int i = 1; i < A.length; i++) {
#             last = intersection(last, count(A[i]));
#         }
#         List<String> arr = new ArrayList<>();
#         for (int i = 0; i < 26; i++) {
#             if (last[i] != 0) {
#                 char a = 'a';
#                 a += i;
#                 String s = String.valueOf(a);
#                 while (last[i] > 0) {
#                     arr.add(s);
#                     last[i]--;
#                 }
#             }
#         }
#         return arr;
#     }
#     int[] intersection(int[] a, int[] b) {
#         int[] t = new int[26];
#         for (int i = 0; i < 26; i++) {
#             t[i] = Math.min(a[i], b[i]);
#         }
#         return t;
#     }
#     int[] count(String str) {
#         int[] t = new int[26];
#         for (char c : str.toCharArray()) t[c - 'a']++;
#         return t;
#     }
# }
