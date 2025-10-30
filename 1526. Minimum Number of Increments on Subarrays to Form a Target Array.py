
class Solution:
    def build(self, ind, low, high, target):
        if low == high:
            self.seg[ind] = (target[low], low) 
            return
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid, target)
        self.build(2 * ind + 2, mid + 1, high, target)
        self.seg[ind] = min(self.seg[2 * ind + 1], self.seg[2 * ind + 2])

    def query(self, ind, low, high, l, r):
        if high < l or low > r:  
            return (sys.maxsize, sys.maxsize)
        if l <= low and high <= r:  
            return self.seg[ind]

        mid = (low + high) // 2  # Partial overlap
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return min(left, right)

    def minNumberOperations(self, target):
        n = len(target)
        self.seg = [None] * (4 * n)
        self.build(0, 0, n - 1, target)

        ans = 0
        q = deque()
        q.append((0, n - 1, 0))  

        while q:
            l, r, level = q.popleft()
            mini, idx = self.query(0, 0, n - 1, l, r)
            ans += (mini - level)
            if idx - 1 >= l:
                q.append((l, idx - 1, mini))
            if idx + 1 <= r:
                q.append((idx + 1, r, mini))

        return ans


#in cpp
class Solution {
public:
    vector<pair<int,int>> seg;

    // Build the segment tree
    void build(int ind, int low, int high, vector<int>& target){
        if(low == high){
            seg[ind] = {target[low], low}; // {MIN VALUE, INDEX}
            return;
        }
        int mid = (low + high)/2;
        build(2*ind+1, low, mid, target);
        build(2*ind+2, mid+1, high, target);
        seg[ind] = min( seg[2*ind+1], seg[2*ind+2] );
        return;
    }

    // Find the {minimum value, index} from range l to r
    pair<int,int> query(int ind, int low, int high, int l, int r, vector<int>& target){
        if(high < l || low > r) return {INT_MAX, INT_MAX}; // NO OVERLAP
        if( low >= l && high <= r ) return seg[ind]; // COMPLETE OVERLAP

        int mid = (low + high)/2; // PARTIAL OVERLAP
        auto left = query(2*ind+1, low, mid, l, r, target); // MIN OF LEFT HALF
        auto right = query(2*ind+2, mid+1, high, l,r, target); // MIN OF RIGHT HALF

        return min(left, right); // MIN OF BOTH
    }

    int minNumberOperations(vector<int>& target) {
        int n = target.size();
        seg.resize(4*n);
        build(0,0,n-1, target); // build the segment tree

        int ans = 0;
        queue<vector<int>> q;
        q.push({0,n-1,0}); // LEFT LIMIT | RIGHT LIMIT | BASE LEVEL
        while(!q.empty()){
            auto it = q.front();
            q.pop();
            int l = it[0], r = it[1], level = it[2];
            auto que = query(0,0,n-1,l,r,target);
            int mini = que.first, ind = que.second;
            ans += (mini - level); // add the extra increment needed from base level
            if(ind-1 >= l) q.push({l, ind-1, mini}); // push the left half
            if(ind+1 <= r) q.push({ind+1, r, mini}); // push the right half
        }
        return ans;
    }
};
