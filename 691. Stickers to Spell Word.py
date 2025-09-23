
class Solution(object):
    def minStickers(self, stickers, target):
        m = len(stickers)
        mp = [[0]*26 for y in range(m)] 
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1    
        dp = {}
        dp[""] = 0
        
        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1   
            ans = sys.maxint
            for i in xrange(n):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j]) 
                tmp = helper(dp, mp, s)
                if (tmp != -1): 
                    ans = min(ans, 1+tmp)    
            dp[target] = -1 if ans == sys.maxint else ans
            return dp[target]
                
        return helper(dp, mp, target)





#in cpp
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int m = stickers.size();
        vector<vector<int>> mp(m, vector<int>(26, 0));
        unordered_map<string, int> dp;
        // count characters a-z for each sticker 
        for (int i = 0; i < m; i++) 
            for (char c:stickers[i]) mp[i][c-'a']++;
        dp[""] = 0;
        return helper(dp, mp, target);
    }
private:
    int helper(unordered_map<string, int>& dp, vector<vector<int>>& mp, string target) {
        if (dp.count(target)) return dp[target];
        int ans = INT_MAX, n = mp.size();
        vector<int> tar(26, 0);
        for (char c:target) tar[c-'a']++;
        // try every sticker
        for (int i = 0; i < n; i++) {
            // optimization
            if (mp[i][target[0]-'a'] == 0) continue; 
            string s;
            // apply a sticker on every character a-z
            for (int j = 0; j < 26; j++) 
                if (tar[j]-mp[i][j] > 0) s += string(tar[j]-mp[i][j], 'a'+j);
            int tmp = helper(dp, mp, s);
            if (tmp!= -1) ans = min(ans, 1+tmp);
        }
        dp[target] = ans == INT_MAX? -1:ans;
        return dp[target];
    }
};
