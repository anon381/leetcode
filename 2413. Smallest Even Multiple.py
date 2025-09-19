class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        if n%2!=0:
            return 2*n
        
#in cpp
# class Solution {
# public:
#     int smallestEvenMultiple(int n) {
#         if(n%2==0){
#             return n;
#         }
#         else {
#             return 2*n;
#         }

#     }
# };
