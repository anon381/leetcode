class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count





#in cpp
# #include <unordered_set>
# #include <string>
# using namespace std;

# class Solution {
# public:
#     int numJewelsInStones(string jewels, string stones) {
#         unordered_set<char> jewelSet(jewels.begin(), jewels.end());
#         int count = 0;
#         for (char s : stones) {
#             if (jewelSet.count(s)) {
#                 count++;
#             }
#         }
#         return count;
#     }
# };


#in java

