class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
         morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_dict = dict(zip(letters, morse_code))
        words2 = []
        for word in words:
            k = ""            
            for i in word:
                k += morse_dict[i]
            words2.append(k) 
        return len(set(words2))
# in cpp
# class Solution {
# public:
#     int uniqueMorseRepresentations(vector<string>& words) {
#         vector<string> morseCode = {
#             ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
#             "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
#             "..-", "...-", ".--", "-..-", "-.--", "--.."
#         };

#         unordered_set<string> uniqueMorse;

#         for (const string& word : words) {
#             string morseRepresentation = "";
#             for (char c : word) {
#                 morseRepresentation += morseCode[c - 'a'];
#             }
#             uniqueMorse.insert(morseRepresentation);
#         }

#         return uniqueMorse.size();
#     }
# };
