
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        idx = 0
        n = len(bits)
        while idx < n - 1:
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1
        return idx == n - 1
# in cpp
# class Solution {
# public:
#     bool isOneBitCharacter(vector<int>& bits) {
#         int i = 0;
#         while(i < bits.size() - 1){
#             if(bits[i] == 0){
#                 i++;  
#             }else{
               
#                 i+=2;
#             }
#         }
#         return i == bits.size() - 1;
#     }
# };
