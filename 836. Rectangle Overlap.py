class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        return not (
            rec1[2] <= rec2[0] or  
            rec1[0] >= rec2[2] or  
            rec1[3] <= rec2[1] or  
            rec1[1] >= rec2[3]    
        )
