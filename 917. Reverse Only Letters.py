# Complexity
# Time complexity: O(n)

# Space complexity: O(n)


class Solution(object):
    def reverseOnlyLetters(self, s):
        arr = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ''.join(arr)



#in java
# class Solution {
#     public String reverseOnlyLetters(String s) {
#         char[] arr = s.toCharArray();
#         int left = 0, right = s.length() - 1;
#         while(left < right)
#         {
#             while(left < right && !Character.isLetter(arr[left]))
#             {
#                 left ++;
#             }
#             while(left < right && !Character.isLetter(arr[right]))
#             {
#                 right --;
#             }
#             char temp = arr[left];
#             arr[left] = arr[right];
#             arr[right] = temp;
#             left ++;
#             right --;
#         }
#         return new String(arr);
#     }
# }



class Solution {
public:
    string reverseOnlyLetters(string s) {
        int length = s.length();
        int left = 0, right = length - 1;
        string answer = "";
                while (left < length) {
            if (isalpha(s[left]) && isalpha(s[right])) {
                answer += s[right];
                left++;
                right--;
            }
            else if (!isalpha(s[left])) {
                answer += s[left];
                left++;
            }
            else {
                right--;
            }
        }
        return answer;
    }
};
