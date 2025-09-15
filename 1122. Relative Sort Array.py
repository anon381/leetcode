class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []
        
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    arr1[j] = -1
        
        arr1.sort()
        
        for num in arr1:
            if num != -1:
                result.append(num)
                
        return result


#in cpp
# class Solution {
# public:
#     vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
#         vector<int> result;
     
#         for (int i = 0; i < arr2.size(); i++) {
#             for (int j = 0; j < arr1.size(); j++) {   
#                 if (arr1[j] == arr2[i]) {
#                     result.push_back(arr1[j]);
#                     arr1[j] = -1;
#                 }
#             }
#         }
#         sort(arr1.begin(), arr1.end());

#         for (int i = 0; i < arr1.size(); i++) {
#             if (arr1[i] != -1) {
#                 result.push_back(arr1[i]);
#             }
#         }
#         return result;
#     }
# };



#in java
# class Solution {
#     public int[] relativeSortArray(int[] arr1, int[] arr2) {
#         List<Integer> result = new ArrayList<>();
        
#         for (int i = 0; i < arr2.length; i++) {
#             for (int j = 0; j < arr1.length; j++) {
#                 if (arr1[j] == arr2[i]) {
#                     result.add(arr1[j]);
#                     arr1[j] = -1;
#                 }
#             }
#         }
        
#         Arrays.sort(arr1);
        
#         for (int i = 0; i < arr1.length; i++) {
#             if (arr1[i] != -1) {
#                 result.add(arr1[i]);
#             }
#         }
        
#         // Convert List<Integer> to int[]
#         return result.stream().mapToInt(Integer::intValue).toArray();
#     }
# }
