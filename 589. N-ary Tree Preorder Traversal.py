
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        l = []
        while stack:
            node = stack.pop()
            l.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return l
