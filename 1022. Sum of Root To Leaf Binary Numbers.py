class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(u, s):
            nonlocal ans
            if not u:
                return
            s = (s << 1) | u.val
            if not u.left and not u.right:
                ans += s
                return
            dfs(u.left, s)
            dfs(u.right, s)
        ans = 0
        dfs(root, 0)
        return ans
