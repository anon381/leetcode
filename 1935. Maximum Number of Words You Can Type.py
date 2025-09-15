class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        mask = 0
        for ch in broken:
            mask |= 1 << (ord(ch) - 97)
        
        count = 0
        wordMask = 0
        n = len(text)
        for i in range(n + 1):
            if i < n and 'a' <= text[i] <= 'z':
                wordMask |= mask & (1 << (ord(text[i]) - 97))
            if i == n or text[i] == ' ':
                if wordMask == 0:
                    count += 1
                wordMask = 0
        return count


#in cpp
# class Solution {
# public:
#     int canBeTypedWords(string text, string broken) {
#         int mask = 0;
#         for (int i = 0; i < broken.size(); i++)
#             mask |= 1 << (broken[i] - 97);
        
#         int count = 0;
#         int wordMask = 0;
#         for (int i = 0; i <= text.size(); i++) {
#             if (i < text.size() && text[i] >= 'a' && text[i] <= 'z')
#                 wordMask |= mask & (1 << (text[i] - 97));
#             if (i == text.size() || text[i] == ' ') {
#                 if (wordMask == 0) count++;
#                 wordMask = 0;
#             }
#         }
#         return count;
#     }
# };
