class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        def dfs(node):
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = collections.Counter()
        dfs(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]


    

#in cpp
    unordered_map<int, int> count;
    int maxCount = 0;
    vector<int> findFrequentTreeSum(TreeNode* root) {
        dfs(root);
        vector<int> res;
        for (auto & e: count)
            if (e.second == maxCount)
                res.push_back(e.first);
        return res;
    }


    int dfs(TreeNode* root) {
        if (root == NULL) return 0;
        int s = dfs(root->left) + dfs(root->right) + root->val;
        maxCount = max(maxCount, ++count[s]);
        return s;
    }
