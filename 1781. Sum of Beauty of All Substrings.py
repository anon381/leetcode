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



#in java
class Solution {
    public int beautySum(String s) {
        int ans=0;
        for(int i=0;i<s.length();i++){
            int [] freq=new int [26];
            for(int j=i;j<s.length();j++){
                char ch=s.charAt(j);
                freq[ch-'a']++;
                int max=Integer.MIN_VALUE;
                int min=Integer.MAX_VALUE;
                for(int k=0;k<26;k++){
                    if(freq[k]>0){
                        min=Math.min(min,freq[k]);
                        max=Math.max(max,freq[k]);
                    }
                }
                ans+=max-min;
            }
        }
        return ans;
    }
}
