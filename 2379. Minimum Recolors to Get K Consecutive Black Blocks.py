class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        recolor=W=blocks[:k].count('W')
        for l in range(n-k):
            W+=(blocks[l+k]=='W')-(blocks[l]=='W')
            recolor=min(recolor, W)
        return recolor
        

#in cpp
# class Solution {
# public:
#     int minimumRecolors(string& blocks, int k) {
#         const int n=blocks.size();
#         int W=count(blocks.begin(), blocks.begin()+k, 'W');
#         int recolor=W;
#         for(int l=0, r=k; r<n; r++, l++){
#             W+=(blocks[r]=='W')-(blocks[l]=='W');
#             recolor=min(recolor, W);
#         }
#         return recolor;
#     }
# };
