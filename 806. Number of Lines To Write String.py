class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_lines = 1
        current_width = 0
        
        for char in s:
            char_index = ord(char) - ord('a')  
            char_width = widths[char_index]    
            
            if current_width + char_width > 100:
                total_lines += 1      
                current_width = char_width  
            else:
                current_width += char_width 
        
        return [total_lines, current_width]

   
# or in cpp
# class Solution {
# public:
#     vector<int> numberOfLines(vector<int>& widths, string s) {
#         int lines = 1, remain = 0;
#         for(int i = 0, n = s.length(); i < n; ++i){
#             if(remain + widths[s[i] - 'a'] <= 100) remain += widths[s[i] - 'a'];
#             else {
#                 ++lines;
#                 remain = widths[s[i] - 'a'];
#             }
#         }
#         return {lines , remain};
#     }
# };
