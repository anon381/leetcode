
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Read the Main Method, before reading the helper Method.

        # Helper Method:
        # DFS, Checking whether two trees are same
        def dfs_sameTree(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    return dfs_sameTree(node1.left, node2.left) and dfs_sameTree(node1.right, node2.right)
            elif not node1 and not node2:
                return True
            else:
                return False


        # Main Method:
        # Finding the matching root for the subRoot
        stack, rootNode = [root], None
        while stack:
            rootNode = stack.pop()
            if not rootNode: continue

            # Once we have a match,  We check whether they are same tree.
            if rootNode.val == subRoot.val and dfs_sameTree(rootNode, subRoot): 
                return True
                
            stack.append(rootNode.right)
            stack.append(rootNode.left)

        return False
