class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        while k:
            k, a = divmod(k, 10)
            num = [a] + num
        return num


#in cpp
# class Solution {
# public:
#     vector<int> addToArrayForm(vector<int>& num, int k) {
#         for(int i=num.size()-1;i>=0;i--){
#             num[i] += k;
#             k = num[i]/10;
#             num[i] %= 10;
#         }
#         while(k > 0){
#             num.insert(num.begin(), k%10);
#             k /= 10;
#         }
#         return num;
#     }
# };
