class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0  
        def calculate_tilt(node):
            if not node:
                return 0 
            left_sum = calculate_tilt(node.left)
            right_sum = calculate_tilt(node.right)
            tilt = abs(left_sum - right_sum)
            #calculate the sums and tilt
            self.total_tilt += tilt
            #return the sum
            return left_sum + right_sum + node.val
        #calculate tilt
        calculate_tilt(root)
        return self.total_tilt
