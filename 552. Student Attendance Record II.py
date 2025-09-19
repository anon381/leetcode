# Time Complexity: 
# 𝑂(𝑛)
#  (because memoization ensures each state is computed only once)

class Solution:
    def checkRecord(self, n: int) -> int:
        temp: list[list[list[int]]] = [
            [[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)
        ]  # temp[cur_ind][count_a][count_l]
        MOD: int = 10**9 + 7

        def check_all_records(cur_ind, count_a, count_l) -> int:
            if cur_ind == n:
                return 1
            if temp[cur_ind][count_a][count_l] != -1:
                return temp[cur_ind][count_a][count_l]
            with_a_next: int = check_all_records(cur_ind + 1, count_a + 1, 0) if count_a == 0 else 0
            with_l_next: int = 0 if count_l == 2 else check_all_records(cur_ind + 1, count_a, count_l + 1)
            with_p_next: int = check_all_records(cur_ind + 1, count_a, 0)
            total: int = (with_a_next + with_l_next + with_p_next) % MOD

            temp[cur_ind][count_a][count_l] = total
            return total

        return check_all_records(0, 0, 0)




#in cpp



#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int checkRecord(int n) {
        const int MOD = 1e9 + 7;
        // temp[cur_ind][count_a][count_l]
        vector<vector<vector<int>>> memo(n, vector<vector<int>>(2, vector<int>(3, -1)));

        function<int(int, int, int)> dfs = [&](int day, int a_count, int l_count) -> int {
            if(day == n) return 1;
            if(memo[day][a_count][l_count] != -1) return memo[day][a_count][l_count];

            int res = 0;
            // Add 'A'
            if(a_count == 0) res = (res + dfs(day+1, 1, 0)) % MOD;
            // Add 'L'
            if(l_count < 2) res = (res + dfs(day+1, a_count, l_count+1)) % MOD;
            // Add 'P'
            res = (res + dfs(day+1, a_count, 0)) % MOD;

            return memo[day][a_count][l_count] = res;
        };

        return dfs(0, 0, 0);
    }
};



#in java
class Solution {
    private final int MOD = 1_000_000_007;
    private int[][][] memo;

    public int checkRecord(int n) {
        memo = new int[n][2][3];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < 2; j++)
                Arrays.fill(memo[i][j], -1);
        return dfs(0, 0, 0, n);
    }

    private int dfs(int day, int a_count, int l_count, int n) {
        if(day == n) return 1;
        if(memo[day][a_count][l_count] != -1) return memo[day][a_count][l_count];

        int res = 0;
        if(a_count == 0) res = (res + dfs(day + 1, 1, 0, n)) % MOD;
        if(l_count < 2) res = (res + dfs(day + 1, a_count, l_count + 1, n)) % MOD;
        res = (res + dfs(day + 1, a_count, 0, n)) % MOD;

        return memo[day][a_count][l_count] = res;
    }
}
