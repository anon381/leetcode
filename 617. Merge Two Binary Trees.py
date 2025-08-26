class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
# or in cpp
# class Solution {
# public:
#     TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
#         if (!root1) return root2;
#         if (!root2) return root1;
#         root1->val += root2->val;
#         root1->left = mergeTrees(root1->left, root2->left);
#         root1->right = mergeTrees(root1->right, root2->right);
#         return root1;
#     }
# };
