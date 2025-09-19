
# Complexity

# Time complexity: O(2 ^n)
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        self.target_length = n
        
        def find_min_steps(current_length: int, clipboard_length: int) -> int:
            if current_length == self.target_length:
                return 0
            if current_length > self.target_length:
                return float('inf')
            
            copy_and_paste = 2 + find_min_steps(current_length * 2, current_length)
            paste_only = 1 + find_min_steps(current_length + clipboard_length, clipboard_length)
            
            return min(copy_and_paste, paste_only)
        
        return 1 + find_min_steps(1, 1)

#in cpp
class Solution {
private:
    int targetLength;

    int findMinSteps(int currentLength, int clipboardLength) {
        if (currentLength == targetLength) return 0;
        if (currentLength > targetLength) return INT_MAX / 2;

        int copyAndPaste = 2 + findMinSteps(currentLength * 2, currentLength);
        int pasteOnly = 1 + findMinSteps(currentLength + clipboardLength, clipboardLength);

        return std::min(copyAndPaste, pasteOnly);
    }

public:
    int minSteps(int n) {
        if (n == 1) return 0;
        targetLength = n;
        return 1 + findMinSteps(1, 1);
    }
};


#in java
class Solution {
    private int targetLength;
    
    public int minSteps(int n) {
        if (n == 1) return 0;
        this.targetLength = n;
        return 1 + findMinSteps(1, 1);
    }
    
    private int findMinSteps(int currentLength, int clipboardLength) {
        if (currentLength == targetLength) return 0;
        if (currentLength > targetLength) return Integer.MAX_VALUE / 2;
        
        int copyAndPaste = 2 + findMinSteps(currentLength * 2, currentLength);
        int pasteOnly = 1 + findMinSteps(currentLength + clipboardLength, clipboardLength);
        
        return Math.min(copyAndPaste, pasteOnly);
    }
}
