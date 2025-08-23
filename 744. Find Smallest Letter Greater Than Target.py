
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left] if left < len(letters) else letters[0]
# or cpp file added

# #include <vector>
# using namespace std;

# class Solution {
# public:
#     char nextGreatestLetter(vector<char>& letters, char target) {
#         int left = 0, right = letters.size() - 1;

#         while(left <= right) {
#             int mid = left + (right - left) / 2;
#             if(letters[mid] <= target) {
#                 left = mid + 1;
#             } else {
#                 right = mid - 1;
#             }
#         }
#         // if left is out of range, wrap to first
#         return (left < letters.size()) ? letters[left] : letters[0];
#     }
# };
