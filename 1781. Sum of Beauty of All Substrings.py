# Complexity
# Time complexity: O(n ^ 2)
# Space complexity: O(1)

class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i, len(s)):
                freq[s[j]] += 1
                total_beauty += max(freq.values()) - min(freq.values())
        return total_beauty


#in cpp
class Solution {
public:
    int beautySum(string s) {
        int beautysum = 0;
        unordered_map<char,int> mp;
    
        for(int i=0; i<s.size(); i++){
            mp.clear();
            for(int j=i; j<s.size(); j++){
                char &ch = s[j];
                mp[ch]++;
                int maxi = INT_MIN;
                int mini = INT_MAX;
                for(auto each:mp){
                    maxi = max(maxi,each.second);
                    mini = min(mini,each.second);
                }
                int beauty = maxi-mini;
                beautysum += beauty;
            }
        }
        return beautysum;
    }
};
