#Complexity
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:        
        res = 0

        def count_palindrome(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count

        for i in range(len(s)):
            res += count_palindrome(s, i, i)
            res += count_palindrome(s, i, i + 1)
        
        return res

#in cpp
class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;

        for (int i = 0; i < s.length(); i++) {
            res += count_palindrome(s, i, i);
            res += count_palindrome(s, i, i + 1);
        }

        return res;        
    }

private:
    int count_palindrome(string s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }
        return count;
    }

};

#in java
class Solution {
    public int countSubstrings(String s) {
        int res = 0;

        for (int i = 0; i < s.length(); i++) {
            res += count_palindrome(s, i, i);
            res += count_palindrome(s, i, i + 1);
        }

        return res;        
    }

    private int count_palindrome(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            count++;
            left--;
            right++;
        }
        return count;
    }

}
