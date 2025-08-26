from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        res, queue = [], deque([root])

        while queue:
            level_sum = 0
            count = len(queue)

            for _ in range(count):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(level_sum / count)

        return res
# or in cpp
# class Solution {
# public:
#     vector<double> averageOfLevels(TreeNode* root) {
#         vector<double> ans;
#         queue<TreeNode*> q;

#         q.push(root);

#         while (!q.empty()) {
#             int n = q.size();
#             double sum = 0;

#             for (int i = 0; i < n; ++i) {
#                 TreeNode* curnode = q.front();
#                 q.pop();

#                 sum += curnode->val;

#                 if (curnode->left)
#                     q.push(curnode->left);

#                 if (curnode->right)
#                     q.push(curnode->right);
#             }
#             ans.push_back(sum / n);
#         }

#         return ans;
#     }
# };
