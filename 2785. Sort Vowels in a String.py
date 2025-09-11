
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        s_list = list(s)
        for i in s_list:
            if i in "AEIOUaeiou":
                vowels.append(i)
        
        if vowels == []:
            return s
        vowels.sort()

        count = 0

        for j in range(len(s)):
            if s_list[j] in "AEIOUaeiou":
                s_list[j] = vowels[count]
                count += 1

        return "".join(s_list)


#in cpp

# class Solution {
# public:
#     string sortVowels(string s) {
#         vector<char> vowels;
#         for (char c : s) {
#             if (isVowel(c)) {
#                 vowels.push_back(c);
#             }
#         }

#         sort(vowels.begin(), vowels.end());

#         int v_index = 0;
#         for (int i = 0; i < s.size(); i++) {
#             if (isVowel(s[i])) {
#                 s[i] = vowels[v_index++];
#             }
#         }

#         return s;
#     }

# private:
#     bool isVowel(char c) {
#         return string("AEIOUaeiou").find(c) != string::npos;
#     }
# };



#in java
# class Solution {
#     public String sortVowels(String s) {
#         List<Character> vowels = new ArrayList<>();
#         for (char c : s.toCharArray()) {
#             if ("AEIOUaeiou".indexOf(c) != -1) {
#                 vowels.add(c);
#             }
#         }

#         Collections.sort(vowels);

#         StringBuilder result = new StringBuilder();
#         int vIndex = 0;
#         for (char c : s.toCharArray()) {
#             if ("AEIOUaeiou".indexOf(c) != -1) {
#                 result.append(vowels.get(vIndex++));
#             } else {
#                 result.append(c);
#             }
#         }

#         return result.toString();
#     }
# }
