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

   
