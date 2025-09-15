class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(arr2)
        dict_pre = {0: -float("inf")}
        for num in arr1:
            dict_cur = collections.defaultdict(lambda: float("inf"))
            for n_swap in dict_pre:
                if num > dict_pre[n_swap]:
                    dict_cur[n_swap] = min(dict_cur[n_swap], num)
                loc = bisect.bisect(arr2, dict_pre[n_swap])
                if loc < len(arr2):
                    dict_cur[n_swap+1] = min(dict_cur[n_swap+1], arr2[loc]) 
            if not dict_cur:
                return -1
            dict_pre = dict_cur
        return min(dict_pre.keys())
		
		
#IN CPP
//class Solution {
// public:
//     int solve(int i,int j,int &a,int &b,int p,vector<vector<int>> &dp,vector<int> &v1,vector<int> &v2){
//         if(i==a){
//             return 0;
//         }
//         j = upper_bound(v2.begin()+j,v2.end(),p)-v2.begin();
//         if(dp[i][j] != -1)return dp[i][j];
//         if(j==b && v1[i]<=p)return 2001;
//         int take = 2001,nottake = 2001;
//         if(j!=b)
//         take = solve(i+1,j+1,a,b,v2[j],dp,v1,v2)+1;
//         if(v1[i]>p)
//         nottake = solve(i+1,j,a,b,v1[i],dp,v1,v2);
//         return dp[i][j] = min(take,nottake);
//     }
//     int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
//         int n = arr1.size(),m=arr2.size();
//         vector<vector<int>> dp(2001,vector<int>(2001,-1));
//         sort(arr2.begin(),arr2.end());
//         int a= solve(0,0,n,m,-1,dp,arr1,arr2);
//         if(a>n)return -1;
//         return a;
//     }
// };
