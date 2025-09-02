
# Complexity
# Time complexity:
# O(n), where n is the length of the typed string. This is because of a single loop that iterates through the typed string.

# Space complexity:
# O(1). The solution uses a constant amount of space for the pointers i and j, and does not use any additional data structures that grow with the input size.



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
            
        return i == len(name)



# in cpp
# class Solution {
# public:
#     bool isLongPressedName(string name, string typed) {
#         int i = 0, j = 0;

#         while(j < typed.size()){
#             if(i < name.size() && name[i] == typed[j]){
#                 i++;
#                 j++;
#             }
#             else if(j > 0 && typed[j] == typed[j - 1]){
#                 j++;
#             }
#             else{
#                 return false;
#             }
#         }

#         return i == name.size();
#     }
# };




# in java
# class Solution {
#     public boolean isLongPressedName(String name, String typed) {
#         if(name.charAt(0)!=typed.charAt(0)){
#             return false;
#         }
#         if(name.length()>typed.length()){
#             return false;
#         }
#         int i=1;
#         int j=1;
#         while(j<typed.length()){
#             if(i<name.length() && name.charAt(i)==typed.charAt(j)){
#                 i++;
#                 j++;
#             }
#             else if (typed.charAt(j)==typed.charAt(j-1)){
#                 j++;
#             }
#             else{
#                 return false;
#             }
#         }
#         return i==name.length();
#     }
# }
