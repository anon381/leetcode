# Complexity
# Time Complexity =  O(n)
# Space Complexity = O(1)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

#in cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int zeroes = count(arr.begin(), arr.end(), 0);

        for (int i = n - 1; i >= 0; i--) {
            if (i + zeroes < n) {
                arr[i + zeroes] = arr[i];
            }
            if (arr[i] == 0) {
                zeroes--;
                if (i + zeroes < n) {
                    arr[i + zeroes] = 0;
                }
            }
        }
    }
};
