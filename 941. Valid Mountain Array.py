"""
Complexity Analysis:
    - Time Complexity: O(n)
    - Space Complexity: O(1)
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1




# in cpp
# class Solution {
# public:
#     bool validMountainArray(vector<int>& arr) {
#         int length = arr.size();
#         int counter = 0; 
#         for (int i = 0; i < length - 1; i++) {
#             if (counter == 0) {
#                 if (arr[i] > arr[i + 1]) {     
#                     counter = 1;
#                 } else if (arr[i] == arr[i + 1]) {
#                     return false;             
#                 }
#             }
#             if (counter == 1) {
#                 if (arr[i] <= arr[i + 1])
#                     return false;              
#             }
#         }
#         if (length > 1 && arr[0] > arr[1])
#             return false;                      
#         return counter == 1;                  
#     }
# };




#in java
# class Solution {
#     public boolean validMountainArray(int[] arr) {
#         if(arr.length < 3) return false;
#         int l = 0;
#         int r = arr.length - 1;
#         while(l + 1 < arr.length - 1 && arr[l] < arr[l + 1]) l++;
#         while(r - 1 > 0 && arr[r] < arr[r - 1]) r--;
#         return l == r;
#     }
# }
