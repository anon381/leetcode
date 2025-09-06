class Solution:
    def increasingBST(self, node: TreeNode) -> TreeNode:
        dummy = tail = TreeNode()
        while node is not None:
            if node.left is not None:
                predecessor = node.left
                while predecessor.right is not None:
                    predecessor = predecessor.right
                
                predecessor.right = node
                left, node.left = node.left, None
                node = left
            else:
                tail.right = tail = node
                node = node.right
        
        return dummy.right



#in cpp

# class Solution {
# public:
#     TreeNode* increasingBST(TreeNode* node) {
#         TreeNode dummy(0);
#         TreeNode* tail = &dummy;

#         while (node != nullptr) {
#             if (node->left != nullptr) {
#                 TreeNode* predecessor = node->left;
#                 while (predecessor->right != nullptr) {
#                     predecessor = predecessor->right;
#                 }
#                 predecessor->right = node;
#                 TreeNode* left = node->left;
#                 node->left = nullptr;
#                 node = left;
#             } else {
#                 tail->right = node;
#                 tail = node;
#                 node = node->right;
#             }
#         }
#         return dummy.right;
#     }
# };
