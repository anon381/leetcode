class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        n = len(deck)
        result = [0] * n
        indices = deque(range(n))
        
        for card in deck:
            idx = indices.popleft()
            result[idx] = card
            if indices:
                indices.append(indices.popleft())

        return result

# C++ version of the above Python code:
#
# #include <vector>
# #include <deque>
# #include <algorithm>
# using namespace std;
# class Solution {
# public:
#     vector<int> deckRevealedIncreasing(vector<int>& deck) {
#         sort(deck.begin(), deck.end());
#         int n = deck.size();
#         deque<int> indices;
#         for (int i = 0; i < n; ++i) indices.push_back(i);
#         vector<int> result(n);
#         for (int card : deck) {
#             int idx = indices.front(); indices.pop_front();
#             result[idx] = card;
#             if (!indices.empty()) {
#                 indices.push_back(indices.front()); indices.pop_front();
#             }
#         }
#         return result;
#     }
# };