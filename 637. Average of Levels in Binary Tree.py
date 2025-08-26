
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
