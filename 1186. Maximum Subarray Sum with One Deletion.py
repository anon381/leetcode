
#Complexity
# Time complexity: O(N)
# Space complexity: O(N)


#in python 3
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp0 = [0] * n  
        dp1 = [0] * n  
        dp0[0] = arr[0]
        dp1[0] = -10**9  
        res = arr[0]
        for i in range(1, n):
            dp0[i] = max(dp0[i-1] + arr[i], arr[i])
            dp1[i] = max(dp1[i-1] + arr[i], dp0[i-1])
            res = max(res, max(dp0[i], dp1[i]))
        return res

# or

#in python
class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        prev0, prev1 = arr[0], -10**9
        res = arr[0]
     for i in range(1, n):
        dp0 = max(prev0 + arr[i], arr[i])
        dp1 = max(prev1 + arr[i], prev0)
        res = max(res, max(dp0, dp1))           
        prev0, prev1 = dp0, dp1

     return res
    
       



#in cpp
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int n = arr.size();
        vector<int> dp0(n, 0); //Max subarray sum till index i
        vector<int> dp1(n, 0); //Max subarray sum till index i if one element deleted

        dp0[0] = arr[0];
        dp1[0] = -1e9;

        int res = arr[0];
        for(int i = 1; i < n; i++){
            dp0[i] = max(dp0[i-1] + arr[i], arr[i]);

            dp1[i] = max(dp1[i-1] + arr[i], dp0[i-1]);
            res = max(res, max(dp0[i], dp1[i]));
        }
        return res;

    }
};




#in java
class Solution {
    public int maximumSum(int[] arr) {
        int n = arr.length;
        int[] dp0 = new int[n]; // max subarray sum till index i (no deletion)
        int[] dp1 = new int[n]; // max subarray sum till index i (one deletion)

        dp0[0] = arr[0];
        dp1[0] = (int)-1e9; // very small number

        int res = arr[0];
        for (int i = 1; i < n; i++) {
            dp0[i] = Math.max(dp0[i - 1] + arr[i], arr[i]);
            dp1[i] = Math.max(dp1[i - 1] + arr[i], dp0[i - 1]);
            res = Math.max(res, Math.max(dp0[i], dp1[i]));
        }
        return res;
    }
}
