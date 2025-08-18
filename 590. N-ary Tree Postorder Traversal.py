class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        res = []
        def dfs(root):
            for x in root.children:
                dfs(x)
            res.append(root.val)
        dfs(root)
        return res
