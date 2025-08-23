from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image  # no change needed

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != start_color:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
        
# or in cpp if needed

# #include <vector>
# using namespace std;

# class Solution {
# public:
#     vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
#         int startColor = image[sr][sc];
#         if(startColor == color) return image;  // no change needed

#         dfs(image, sr, sc, startColor, color);
#         return image;
#     }

# private:
#     void dfs(vector<vector<int>>& image, int r, int c, int startColor, int newColor) {
#         int m = image.size();
#         int n = image[0].size();

#         // out of bounds or not matching startColor → stop
#         if(r < 0 || r >= m || c < 0 || c >= n || image[r][c] != startColor) return;

#         image[r][c] = newColor;  // recolor

#         // explore neighbors
#         dfs(image, r + 1, c, startColor, newColor);
#         dfs(image, r - 1, c, startColor, newColor);
#         dfs(image, r, c + 1, startColor, newColor);
#         dfs(image, r, c - 1, startColor, newColor);
#     }
# };
