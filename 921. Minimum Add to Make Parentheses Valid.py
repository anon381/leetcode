
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0
        for c in s:
            if c == '(':
                open_c += 1
            elif c == ')' and open_c > 0:
                open_c -= 1
            else:
                close_c += 1
        return open_c + close_c

#in java
class Solution {
    public int minAddToMakeValid(String s) {
        int open_c = 0;
        int close_c = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                open_c++;
            } else if (c == ')' && open_c > 0) {
                open_c--;
            } else {
                close_c++;
            }
        }
        return open_c + close_c;
    }
}

#in cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int open_c = 0;
        int close_c = 0;

        for (char c : s) {
            if (c == '(') {
                open_c++;
            } else if (c == ')' && open_c > 0) {
                open_c--;
            } else {
                close_c++;
            }
        }
        return open_c + close_c;
    }
};
