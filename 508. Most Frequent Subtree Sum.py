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
