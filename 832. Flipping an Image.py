class Solution(object):
    def flipAndInvertImage(self, image):
        for i in  image:
            l,r=0,len(image)-1
            while l<=r:
                if l==r:
                    i[l]=1-i[l]
                else:
                    i[l],i[r]=1-i[r],1-i[l]
                l+=1
                r-=1
        return  image
