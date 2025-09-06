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
