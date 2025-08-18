class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node: TreeNode) -> list[int]:
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_values = inorder(root)
        min_diff = float('inf')
        for i in range(1, len(sorted_values)):
            min_diff = min(min_diff, sorted_values[i] - sorted_values[i - 1])
        return min_diff
