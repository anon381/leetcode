class Solution(object):
    def flipAndInvertImage(self, image):
        for i in  image:
            l,r=0,len(image)-1
            while l<=r:
                if l==r:
                    i[l]=1-i[l]
                else:
                    i[l],i[r]=1-i[r],1-i[l]
                l+=1
                r-=1
        return  image

#in cpp
# class Solution {
# public:
#     vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
#         int n = image.size();
#         for (int i = 0; i < n; i++) {
#             int m = image[i].size();
#             for (int j = 0; j < m / 2; j++) {
#                 swap(image[i][j], image[i][m - 1 - j]);
#             }
#         }

#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < image[i].size(); j++) {
#                 if (image[i][j] == 0)
#                     image[i][j] = 1;
#                 else
#                     image[i][j] = 0;
#             }
#         }

#         return image;
#     }
# };

# in java 
# class Solution {
#     public boolean lemonadeChange(int[] bills) {
#         int five_dollars = 0, ten_dollars = 0;

#         for (int x : bills) {
#             if (x == 5) {
#                 five_dollars++;
#             } else if (x == 10) {
#                 if (five_dollars > 0) {
#                     five_dollars--;
#                     ten_dollars++;
#                 } else {
#                     return false;
#                 }
#             } else {
#                 if (five_dollars > 0 && ten_dollars > 0) {
#                     five_dollars--;
#                     ten_dollars--;
#                 } else if (five_dollars > 2) {
#                     five_dollars -= 3;
#                 } else {
#                     return false;
#                 }
#             }
#         }

#         return true;
#     }
# }
