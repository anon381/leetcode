
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for x in range(lowLimit, highLimit + 1):
            count = 0
            while x:
                count += x % 10
                x //= 10
            d[count] += 1

        return max(d.values())


#in cpp
# class Solution {
# public:
#     int countBalls(int lowLimit, int highLimit) {
#         unordered_map<int,int> mp;

#         int maxi = -1;
#         for(int i=lowLimit;i<=highLimit;i++){
#             int val = i;
#             int sum = 0;

#             while(val!=0){
#                 sum += val%10;
#                 val /= 10;
#             }
#             mp[sum]++;
#             maxi = max(maxi,mp[sum]);
#         }
#         return maxi;
        
#     }
# };
