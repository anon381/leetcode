class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        k = 0
        while candies > 0:
            if candies >= (k+1):
                candies -= (k+1)
                ans[k % num_people] += k + 1
            else:
                ans[k % num_people] += candies
                candies = 0
            k += 1
        return ans


# c++ version
# class Solution {
# public:
#     vector<int> distributeCandies(int candies, int num_people) {
#         vector<int> result(num_people);
#         for (int give = 1, i = 0; candies > 0; ++i , ++give){
#             if(i == num_people) i = 0;
#             result[i] += min(give , candies);
#             candies -= give;
#         }
#         return result;
#     }
# };



#java version
# class Solution {
#     public int[] distributeCandies(int candies, int num_people) {
#         int[] a=new int[num_people];
#         int j=0;
#         while(candies>0)
#         {
#         for(int i=0;i<num_people && candies>0;i++)
#         {
#             j++;
#             int n=Math.min(j,candies);
#             a[i]+=n;
#             candies-=n;
#         }
#         }
#         return a;
#     }
# }
