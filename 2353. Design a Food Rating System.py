
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}  
        self.cuisine_heaps = {}  

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating_neg, food = heap[0]
            if self.food_info[food][1] == -rating_neg:
                return food
            heapq.heappop(heap)  
        return ""  
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)




#in cpp
# class FoodRatings {
#     using item=pair<int, string>;//(rating, food), (rating, cuisine)
#     unordered_map<string, set<item>> Rated;
#     unordered_map<string, item> mp;
# public:
#     FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings)
#     {
#         int n=foods.size();
#         for(int i=0; i<n; i++){
#             string food=foods[i], cuisine=cuisines[i];
#             int rating=ratings[i];
#             mp[food]={-rating, cuisine};//take minus
#             Rated[cuisine].insert({-rating, food});
#         }
#     }
    
#     void changeRating(string food, int newRating) {
#         string& cuisine = mp[food].second;
#         int i = mp[food].first;
#         Rated[cuisine].erase({i, food});
#         Rated[cuisine].insert({-newRating, food});
#         mp[food]={-newRating, cuisine};
#     }
    
#     string highestRated(string cuisine) {
#         return Rated[cuisine].begin()->second;
#     }

# };

# /**
#  * Your FoodRatings object will be instantiated and called as such:
#  * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
#  * obj->changeRating(food,newRating);
#  * string param_2 = obj->highestRated(cuisine);
#  */
#  auto init = []()
# { 
#     ios::sync_with_stdio(0);
#     cin.tie(0);
#     cout.tie(0);
#     return 'c';
# }();




#in java
# import java.util.*;

# class FoodRatings {
#     private Map<String, String> foodToCuisine = new HashMap<>();
#     private Map<String, Integer> foodToRating = new HashMap<>();
#     private Map<String, TreeSet<String>> cuisineFoods = new HashMap<>();

#     public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
#         for (int i = 0; i < foods.length; i++) {
#             foodToCuisine.put(foods[i], cuisines[i]);
#             foodToRating.put(foods[i], ratings[i]);
#         }

#         for (int i = 0; i < foods.length; i++) {
#             String cuisine = cuisines[i];
#             cuisineFoods.putIfAbsent(cuisine, new TreeSet<>((a, b) -> {
#                 int r1 = foodToRating.get(a);
#                 int r2 = foodToRating.get(b);
#                 if (r1 != r2) return r2 - r1; // higher rating first
#                 return a.compareTo(b); // lex order
#             }));
#             cuisineFoods.get(cuisine).add(foods[i]);
#         }
#     }

#     public void changeRating(String food, int newRating) {
#         String cuisine = foodToCuisine.get(food);
#         TreeSet<String> set = cuisineFoods.get(cuisine);

#         set.remove(food);
#         foodToRating.put(food, newRating);
#         set.add(food);
#     }

#     public String highestRated(String cuisine) {
#         return cuisineFoods.get(cuisine).first();
#     }
# }
